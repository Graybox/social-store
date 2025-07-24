import { Button } from '@/components/ui/button';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Badge } from '@/components/ui/badge';
import { ArrowClockwise, MapPin, WifiSlash, Warning } from '@phosphor-icons/react';

interface StatusBarProps {
  isLoading: boolean;
  isOffline: boolean;
  error: string | null;
  lastUpdated: Date | null;
  hasLocation: boolean;
  onRefresh: () => void;
}

export function StatusBar({ 
  isLoading, 
  isOffline, 
  error, 
  lastUpdated, 
  hasLocation, 
  onRefresh 
}: StatusBarProps) {
  return (
    <div className="w-full max-w-sm mx-auto space-y-3">
      {/* Status Indicators */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          {hasLocation ? (
            <Badge variant="secondary" className="text-xs">
              <MapPin size={12} className="mr-1" />
              Location found
            </Badge>
          ) : (
            <Badge variant="destructive" className="text-xs">
              <MapPin size={12} className="mr-1" />
              No location
            </Badge>
          )}
          
          {isOffline && (
            <Badge variant="outline" className="text-xs">
              <WifiSlash size={12} className="mr-1" />
              Offline
            </Badge>
          )}
        </div>

        <Button
          variant="ghost"
          size="sm"
          onClick={onRefresh}
          disabled={isLoading}
          className="h-8 px-2"
        >
          <ArrowClockwise 
            size={16} 
            className={`${isLoading ? 'animate-spin' : ''}`} 
          />
        </Button>
      </div>

      {/* Error Alert */}
      {error && (
        <Alert variant="destructive">
          <Warning size={16} />
          <AlertDescription className="text-sm">
            {error}
          </AlertDescription>
        </Alert>
      )}

      {/* Last Updated */}
      {lastUpdated && (
        <p className="text-xs text-muted-foreground text-center">
          Last updated: {lastUpdated.toLocaleTimeString('en-IN', {
            hour: '2-digit',
            minute: '2-digit'
          })}
        </p>
      )}
    </div>
  );
}