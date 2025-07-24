import { LocationData, VedicTimeData, ApiResponse } from '@/types/vedic';

export async function getCurrentLocation(): Promise<LocationData> {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error('Geolocation is not supported'));
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const timezoneOffset = getTimezoneOffset();
        
        resolve({
          latitude,
          longitude,
          timezone: timezoneOffset
        });
      },
      (error) => {
        reject(new Error(`Location error: ${error.message}`));
      },
      {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 300000 // 5 minutes
      }
    );
  });
}

function getTimezoneOffset(): string {
  const offset = new Date().getTimezoneOffset();
  const hours = Math.floor(Math.abs(offset) / 60);
  const minutes = Math.abs(offset) % 60;
  const sign = offset <= 0 ? '+' : '-';
  
  return `${sign}${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
}

export async function fetchVedicTime(
  date: string,
  location: LocationData,
  language: string = 'en'
): Promise<ApiResponse> {
  try {
    const params = new URLSearchParams({
      date,
      lat: location.latitude.toString(),
      long: location.longitude.toString(),
      tz: location.timezone,
      lang: language
    });

    // For demo purposes, we'll simulate API response since we don't have a real endpoint
    // In production, this would be: const response = await fetch(`/vedic-time?${params}`);
    
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // Mock response data
    const now = new Date();
    const mockData: VedicTimeData = {
      date: now.toLocaleDateString('hi-IN', { 
        day: '2-digit', 
        month: 'long', 
        year: 'numeric' 
      }),
      weekday: now.toLocaleDateString('hi-IN', { weekday: 'long' }),
      tithi: {
        name: 'शुक्ल चतुर्थी',
        time_range: '04:34 – 05:12'
      },
      nakshatra: 'रोहिणी',
      yoga: 'व्यतीपात',
      karana: 'वणिज',
      sunrise: '06:02',
      sunset: '18:55',
      rahukalam: {
        start: '09:08',
        end: '10:38'
      },
      abhijit_muhurta: {
        start: '12:13',
        end: '13:01'
      },
      ghati: Math.floor(Math.random() * 60),
      vighati: Math.floor(Math.random() * 60),
      festivals: Math.random() > 0.5 ? ['विनायक चतुर्थी'] : []
    };

    return {
      success: true,
      data: mockData
    };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Failed to fetch data'
    };
  }
}

export function getSystemLanguage(): string {
  const lang = navigator.language.toLowerCase();
  const supportedLanguages = ['en', 'hi', 'sa', 'ta', 'te', 'kn', 'ml', 'gu', 'mr', 'bn'];
  
  for (const supported of supportedLanguages) {
    if (lang.startsWith(supported)) {
      return supported;
    }
  }
  
  return 'en';
}

export function formatTime(time: string): string {
  try {
    const [hours, minutes] = time.split(':');
    const date = new Date();
    date.setHours(parseInt(hours), parseInt(minutes));
    
    return date.toLocaleTimeString('en-IN', {
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
  } catch {
    return time;
  }
}