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

    const baseUrl =
      (import.meta as any).env.VITE_ENGINE_BASE_URL || 'http://localhost:8080';
    const response = await fetch(`${baseUrl}/vedic-time?${params.toString()}`);

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    const data: VedicTimeData = await response.json();
    return { success: true, data };
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