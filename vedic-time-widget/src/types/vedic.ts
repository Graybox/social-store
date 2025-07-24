export interface VedicTimeData {
  date: string;
  weekday: string;
  tithi: {
    name: string;
    time_range?: string;
  };
  nakshatra: string;
  yoga?: string;
  karana?: string;
  sunrise: string;
  sunset: string;
  choghadiya?: Array<{
    name: string;
    time: string;
    type: string;
  }>;
  rahukalam: {
    start: string;
    end: string;
  };
  abhijit_muhurta: {
    start: string;
    end: string;
  };
  ghati: number;
  vighati: number;
  festivals?: string[];
}

export interface LocationData {
  latitude: number;
  longitude: number;
  timezone: string;
}

export interface ApiResponse {
  success: boolean;
  data?: VedicTimeData;
  error?: string;
}

export interface AppState {
  isLoading: boolean;
  isOffline: boolean;
  error: string | null;
  lastUpdated: Date | null;
  data: VedicTimeData | null;
  location: LocationData | null;
}