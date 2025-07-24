import { VedicTimeData } from '@/types/vedic';
import { Card } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { Badge } from '@/components/ui/badge';
import { Sun, Moon, Clock, Star, Zap, Sparkles } from '@phosphor-icons/react';

interface VedicTimeDisplayProps {
  data: VedicTimeData;
  isOffline?: boolean;
}

export function VedicTimeDisplay({ data, isOffline = false }: VedicTimeDisplayProps) {
  return (
    <Card className="w-full max-w-sm mx-auto p-4 space-y-4 relative">
      {isOffline && (
        <Badge variant="secondary" className="absolute top-2 right-2 text-xs">
          Offline
        </Badge>
      )}
      
      {/* Top Section - Date and Day */}
      <div className="text-center space-y-1">
        <h1 className="text-lg font-medium text-foreground">
          {data.weekday}
        </h1>
        <p className="text-base text-muted-foreground">
          {data.date}
        </p>
      </div>

      <Separator />

      {/* Middle Section - Main Time Information */}
      <div className="space-y-3">
        {/* Sunrise/Sunset */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Sun size={16} className="text-accent" />
            <span className="text-sm font-medium">Sunrise</span>
          </div>
          <span className="text-sm text-muted-foreground">{data.sunrise}</span>
        </div>
        
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Moon size={16} className="text-accent" />
            <span className="text-sm font-medium">Sunset</span>
          </div>
          <span className="text-sm text-muted-foreground">{data.sunset}</span>
        </div>

        <Separator className="my-2" />

        {/* Tithi */}
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <Moon size={16} className="text-primary" />
            <span className="text-sm font-medium">Tithi</span>
          </div>
          <div className="ml-6">
            <p className="text-sm text-foreground">{data.tithi.name}</p>
            {data.tithi.time_range && (
              <p className="text-xs text-muted-foreground">({data.tithi.time_range})</p>
            )}
          </div>
        </div>

        {/* Nakshatra */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Star size={16} className="text-primary" />
            <span className="text-sm font-medium">Nakshatra</span>
          </div>
          <span className="text-sm text-foreground">{data.nakshatra}</span>
        </div>

        {/* Yoga and Karana */}
        {(data.yoga || data.karana) && (
          <div className="grid grid-cols-2 gap-4">
            {data.yoga && (
              <div className="space-y-1">
                <div className="flex items-center gap-1">
                  <Zap size={14} className="text-primary" />
                  <span className="text-xs font-medium">Yoga</span>
                </div>
                <p className="text-xs text-muted-foreground ml-4">{data.yoga}</p>
              </div>
            )}
            {data.karana && (
              <div className="space-y-1">
                <div className="flex items-center gap-1">
                  <Sparkles size={14} className="text-primary" />
                  <span className="text-xs font-medium">Karana</span>
                </div>
                <p className="text-xs text-muted-foreground ml-4">{data.karana}</p>
              </div>
            )}
          </div>
        )}

        {/* Ghati/Vighati */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Clock size={16} className="text-primary" />
            <span className="text-sm font-medium">Ghati</span>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-sm text-foreground">{data.ghati}</span>
            <span className="text-xs text-muted-foreground">|</span>
            <span className="text-xs font-medium">Vighati:</span>
            <span className="text-sm text-foreground">{data.vighati}</span>
          </div>
        </div>
      </div>

      <Separator />

      {/* Bottom Section - Special Times */}
      <div className="space-y-3">
        {/* Rahukalam */}
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-destructive/20 flex items-center justify-center">
              <div className="w-2 h-2 rounded-full bg-destructive" />
            </div>
            <span className="text-sm font-medium">Rahukalam</span>
          </div>
          <p className="text-sm text-muted-foreground ml-6">
            {data.rahukalam.start} to {data.rahukalam.end}
          </p>
        </div>

        {/* Abhijit Muhurta */}
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <Sparkles size={16} className="text-accent" />
            <span className="text-sm font-medium">Abhijit Muhurta</span>
          </div>
          <p className="text-sm text-muted-foreground ml-6">
            {data.abhijit_muhurta.start} to {data.abhijit_muhurta.end}
          </p>
        </div>

        {/* Festivals */}
        {data.festivals && data.festivals.length > 0 && (
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 rounded-full bg-accent/20 flex items-center justify-center">
                <div className="w-2 h-2 rounded-full bg-accent" />
              </div>
              <span className="text-sm font-medium">Festivals</span>
            </div>
            <div className="ml-6 space-y-1">
              {data.festivals.map((festival, index) => (
                <p key={index} className="text-sm text-foreground">{festival}</p>
              ))}
            </div>
          </div>
        )}
      </div>
    </Card>
  );
}