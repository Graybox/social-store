import { useEffect } from 'react';
import { VedicTimeDisplay } from '@/components/VedicTimeDisplay';
import { StatusBar } from '@/components/StatusBar';
import { LoadingSkeleton } from '@/components/LoadingSkeleton';
import { useVedicTime } from '@/hooks/useVedicTime';
import { Card } from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import { MapPin, RefreshCw } from '@phosphor-icons/react';

function App() {
  const { 
    isLoading, 
    isOffline, 
    error, 
    lastUpdated, 
    data, 
    location, 
    refresh 
  } = useVedicTime();

  // Set page title
  useEffect(() => {
    document.title = 'Vedic Time Widget';
  }, []);

  // Handle dark mode based on system preference
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const updateTheme = (e: MediaQueryListEvent | MediaQueryList) => {
      document.documentElement.classList.toggle('dark', e.matches);
    };
    
    updateTheme(mediaQuery);
    mediaQuery.addEventListener('change', updateTheme);
    
    return () => mediaQuery.removeEventListener('change', updateTheme);
  }, []);

  return (
    <div className="min-h-screen bg-background p-4 flex flex-col items-center justify-center gap-4">
      <div className="w-full max-w-sm space-y-4">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-xl font-semibold text-foreground mb-1">
            Vedic Time
          </h1>
          <p className="text-sm text-muted-foreground">
            Daily astronomical information
          </p>
        </div>

        {/* Status Bar */}
        <StatusBar
          isLoading={isLoading}
          isOffline={isOffline}
          error={error}
          lastUpdated={lastUpdated}
          hasLocation={!!location}
          onRefresh={refresh}
        />

        {/* Main Content */}
        {isLoading && !data ? (
          <LoadingSkeleton />
        ) : data ? (
          <VedicTimeDisplay data={data} isOffline={isOffline} />
        ) : (
          <Card className="w-full max-w-sm mx-auto p-6 text-center space-y-4">
            <div className="space-y-2">
              <MapPin size={48} className="mx-auto text-muted-foreground" />
              <h3 className="text-lg font-medium">Getting Started</h3>
              <p className="text-sm text-muted-foreground">
                Enable location access to view your daily Vedic time information.
              </p>
            </div>
            
            {error && (
              <Alert variant="destructive">
                <AlertDescription className="text-sm">
                  {error}
                </AlertDescription>
              </Alert>
            )}
            
            <Button 
              onClick={refresh} 
              disabled={isLoading}
              className="w-full"
            >
              <RefreshCw size={16} className={`mr-2 ${isLoading ? 'animate-spin' : ''}`} />
              {isLoading ? 'Getting Location...' : 'Enable Location'}
            </Button>
          </Card>
        )}

        {/* Footer */}
        <div className="text-center text-xs text-muted-foreground">
          <p>Updates automatically every hour</p>
          {lastUpdated && (
            <p className="mt-1">
              Next update: {new Date(lastUpdated.getTime() + 60 * 60 * 1000).toLocaleTimeString('en-IN', {
                hour: '2-digit',
                minute: '2-digit'
              })}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;