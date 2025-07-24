# Vedic Time Widget

A lightweight mobile widget that displays daily Vedic time information with GPS location awareness and offline capabilities.

**Experience Qualities**: 
1. **Efficient** - Fast loading with minimal data usage and background processing
2. **Intuitive** - Clear visual hierarchy with recognizable icons and organized sections  
3. **Reliable** - Works offline with cached data and graceful error handling

**Complexity Level**: Light Application (multiple features with basic state)
- Integrates GPS location, API calls, data persistence, and auto-refresh functionality while maintaining simplicity

## Essential Features

**GPS Location Detection**
- Functionality: Auto-detects user's latitude, longitude, and timezone
- Purpose: Provides accurate location-specific Vedic time calculations
- Trigger: App launch or manual refresh
- Progression: Request permission → Get coordinates → Convert timezone → Pass to API
- Success criteria: Location coordinates successfully obtained and formatted

**API Data Fetching**
- Functionality: Retrieves daily Vedic time information from REST endpoint
- Purpose: Gets current astronomical and religious timing data
- Trigger: Location obtained or manual refresh
- Progression: Format API URL → Make GET request → Parse JSON response → Store locally
- Success criteria: Valid JSON response parsed and displayed

**Vedic Time Display**
- Functionality: Shows organized sections of time information with icons
- Purpose: Presents complex astronomical data in digestible format
- Trigger: Successful API response
- Progression: Parse data → Format text → Render sections → Apply styling
- Success criteria: All time information clearly visible and properly formatted

**Auto Refresh System**
- Functionality: Updates data every 60 minutes and allows manual refresh
- Purpose: Keeps information current throughout the day
- Trigger: Timer interval or user tap
- Progression: Check elapsed time → Trigger refresh → Update display → Reset timer
- Success criteria: Data refreshes automatically and manually without user intervention

**Offline Mode**
- Functionality: Displays last successful API response when network unavailable
- Purpose: Ensures widget remains functional without internet
- Trigger: API failure or no network connection
- Progression: Detect failure → Load cached data → Show offline indicator → Retry periodically
- Success criteria: Previous data shown with clear offline status

## Edge Case Handling

- **Location Permission Denied**: Show manual location input option
- **API Timeout/Failure**: Display cached data with retry option
- **Invalid API Response**: Show error message with refresh button
- **Timezone Conversion Error**: Fall back to system timezone
- **System Language Unsupported**: Default to English with error note

## Design Direction

The design should feel spiritual yet modern - incorporating traditional Indian aesthetics with contemporary mobile interface patterns. Minimal interface serves the core purpose of quick information access.

## Color Selection

Analogous color scheme - warm earth tones that evoke traditional Indian spirituality and astronomy.

- **Primary Color**: Deep Saffron `oklch(0.65 0.18 45)` - Represents spirituality and sacred knowledge
- **Secondary Colors**: 
  - Warm Sand `oklch(0.85 0.08 65)` - Supporting background warmth
  - Rich Amber `oklch(0.75 0.15 55)` - Section highlights and accents
- **Accent Color**: Bright Orange `oklch(0.72 0.20 40)` - CTAs and important timing information
- **Foreground/Background Pairings**:
  - Background (Cream White `oklch(0.97 0.02 60)`): Dark Brown text `oklch(0.25 0.05 45)` - Ratio 8.2:1 ✓
  - Card (Warm Sand `oklch(0.92 0.06 65)`): Dark Brown text `oklch(0.25 0.05 45)` - Ratio 6.8:1 ✓  
  - Primary (Deep Saffron `oklch(0.65 0.18 45)`): White text `oklch(0.98 0.01 0)` - Ratio 5.1:1 ✓
  - Accent (Bright Orange `oklch(0.72 0.20 40)`): White text `oklch(0.98 0.01 0)` - Ratio 4.6:1 ✓

## Font Selection

Typography should convey traditional wisdom with modern readability, supporting both English and Devanagari scripts seamlessly.

- **Typographic Hierarchy**:
  - **H1 (Date Header)**: Inter Medium/20px/normal spacing for primary date display
  - **H2 (Section Headers)**: Inter Medium/16px/tight spacing for sunrise, tithi sections  
  - **Body (Time Info)**: Inter Regular/14px/relaxed spacing for detailed timing information
  - **Caption (Labels)**: Inter Medium/12px/wide spacing for icons and secondary labels

## Animations

Subtle functionality-focused animations that provide immediate feedback without distracting from information consumption.

- **Purposeful Meaning**: Gentle fade-ins communicate data loading, subtle scale on tap provides tactile feedback
- **Hierarchy of Movement**: Refresh button gets micro-rotation, new data slides in smoothly, error states pulse gently

## Component Selection

- **Components**: 
  - Card component from shadcn for main container with subtle shadow
  - Button component for refresh action with loading states
  - Separator for section divisions
  - Alert for error/offline states
  - Badge for status indicators (online/offline)
- **Customizations**: 
  - Custom time display components for structured information layout
  - Icon-text pairs for consistent visual rhythm
  - Status indicator component for network/GPS states
- **States**: 
  - Loading: Skeleton placeholders with subtle pulse
  - Error: Red-tinted alert with retry button
  - Offline: Muted styling with cached data indicator
  - Success: Full color with fresh timestamp
- **Icon Selection**: Phosphor icons - Sun/Moon for times, MapPin for location, Refresh for manual update, Wifi/WifiSlash for network status
- **Spacing**: Consistent 16px padding, 12px gaps between sections, 8px for related items
- **Mobile**: Single column layout with collapsible sections, touch-friendly 44px minimum tap targets, optimized for 320px minimum width