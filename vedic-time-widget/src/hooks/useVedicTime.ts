import { useState, useEffect, useCallback } from 'react';
import { useKV } from '@github/spark/hooks';
import { AppState, VedicTimeData, LocationData } from '@/types/vedic';
import { getCurrentLocation, fetchVedicTime, getSystemLanguage } from '@/lib/vedic-api';

const REFRESH_INTERVAL = 60 * 60 * 1000; // 60 minutes

export function useVedicTime() {
  const [cachedData, setCachedData] = useKV<VedicTimeData | null>('vedic-data', null);
  const [cachedLocation, setCachedLocation] = useKV<LocationData | null>('location-data', null);
  const [lastUpdated, setLastUpdated] = useKV<string | null>('last-updated', null);
  
  const [state, setState] = useState<AppState>({
    isLoading: false,
    isOffline: false,
    error: null,
    lastUpdated: null,
    data: null,
    location: null
  });

  // Initialize state from cache
  useEffect(() => {
    setState(prev => ({
      ...prev,
      data: cachedData,
      location: cachedLocation,
      lastUpdated: lastUpdated ? new Date(lastUpdated) : null
    }));
  }, [cachedData, cachedLocation, lastUpdated]);

  const refreshData = useCallback(async (forceRefresh = false) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));

    try {
      // Get location
      let location = cachedLocation;
      
      if (!location || forceRefresh) {
        try {
          location = await getCurrentLocation();
          setCachedLocation(location);
        } catch (locationError) {
          if (!cachedLocation) {
            throw new Error('Location access required. Please enable location services.');
          }
          location = cachedLocation;
        }
      }

      // Check if we need to refresh data
      const now = new Date();
      const shouldRefresh = forceRefresh || 
        !lastUpdated || 
        !cachedData ||
        (now.getTime() - new Date(lastUpdated).getTime()) > REFRESH_INTERVAL;

      if (shouldRefresh && location) {
        const today = new Date().toISOString().split('T')[0];
        const language = getSystemLanguage();
        
        const response = await fetchVedicTime(today, location, language);
        
        if (response.success && response.data) {
          setCachedData(response.data);
          setLastUpdated(now.toISOString());
          
          setState(prev => ({
            ...prev,
            data: response.data!,
            location,
            lastUpdated: now,
            isLoading: false,
            isOffline: false,
            error: null
          }));
        } else {
          throw new Error(response.error || 'Failed to fetch data');
        }
      } else {
        // Use cached data
        setState(prev => ({
          ...prev,
          data: cachedData,
          location,
          lastUpdated: lastUpdated ? new Date(lastUpdated) : null,
          isLoading: false,
          isOffline: !navigator.onLine,
          error: null
        }));
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
      
      setState(prev => ({
        ...prev,
        isLoading: false,
        isOffline: !navigator.onLine,
        error: errorMessage,
        data: cachedData, // Keep showing cached data on error
        location: cachedLocation,
        lastUpdated: lastUpdated ? new Date(lastUpdated) : null
      }));
    }
  }, [cachedData, cachedLocation, lastUpdated, setCachedData, setCachedLocation, setLastUpdated]);

  // Auto-refresh effect
  useEffect(() => {
    refreshData();

    const interval = setInterval(() => {
      refreshData();
    }, REFRESH_INTERVAL);

    // Handle online/offline events
    const handleOnline = () => {
      setState(prev => ({ ...prev, isOffline: false }));
      refreshData();
    };

    const handleOffline = () => {
      setState(prev => ({ ...prev, isOffline: true }));
    };

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      clearInterval(interval);
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, [refreshData]);

  return {
    ...state,
    refresh: () => refreshData(true)
  };
}