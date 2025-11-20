# LanguageForge Release Notes

## Version 1.0.0 – Initial Release (November 2025)

### 🎉 Welcome to LanguageForge!

The first official release of **LanguageForge** – a comprehensive language learning management system for Anki. This release provides a complete toolkit for tracking, planning, and visualizing your language learning journey.

---

### ✨ Core Features

#### 📊 Dashboard – Command Center
- **Unified overview** of all features in one place
- **Fluency Snapshot**: Interactive radar chart showing skill balance across Reading, Listening, Speaking, Writing
- **This Week's Activity**: 4×7 grid for quick daily practice tracking with visual consistency indicators
- **Daily Plan Tasks**: 4 inline editable tasks aligned with skill rows for daily planning
- **This Month's Goals**: Preview of 3 monthly goals with quick completion toggles
- **Learning Resources**: Preview of 5 most recent resources with direct "Open" buttons
- Real-time status updates and auto-save functionality

#### 📈 Daily Tracker
- **Monthly calendar view** for comprehensive activity tracking across all four skills
- **Skills tracked**: Reading, Listening, Speaking, Writing
- Visual circle indicators for each skill/day combination (click to toggle)
- **Statistics dashboard**:
  - Total active days count
  - Longest practice streak
  - Per-skill completion percentages
- Month/year selector for viewing historical data
- Consistency tracking and progress visualization

#### 🎯 Monthly Goals
- **3 goal slots per month** for focused objective setting
- **Rich goal structure**:
  - Goal title and description
  - Category selection (General, Vocabulary, Grammar, Reading, Listening, Speaking, Writing)
  - Unlimited subtasks with individual completion tracking
  - Reflection notes for documenting insights and challenges
  - Automatic timestamps (created/completed dates)
- **Goal management**:
  - Add, edit, and delete goals and subtasks
  - Archive past months (view-only mode)
  - Visual completion indicators throughout
- Inline editing with auto-save

#### 📚 Learning Resources
- **Centralized library** for all learning materials
- **Resource fields**:
  - Title (required)
  - Type (Book, Video, Podcast, Course, Website, App, Other)
  - URL (optional, enables direct "Open" button)
  - Status (Not Started, In Progress, Completed, Reference)
  - Notes (tags, descriptions, thoughts)
- **Features**:
  - Real-time search and filtering
  - One-click URL opening in browser
  - Sortable table view
  - Add/edit/delete functionality
- Auto-save changes

#### 🎭 Fluency Snapshot (Radar Chart)
- **Interactive radar chart** for self-assessment of language proficiency
- **4 skill axes**: Reading, Listening, Speaking, Writing (1-5 scale)
- **Visual features**:
  - Draggable skill values for easy adjustment
  - Ghost polygon showing previous month's values
  - Trend arrows (↑ improved, ↓ declined, = stable)
  - Balance Index (0-100%) measuring skill distribution evenness
- Month selector for viewing historical snapshots
- Save functionality with automatic timestamping

#### 🌍 Multi-Profile System
- **Unlimited profile support** (capped at 50 for safety)
- **Complete data isolation** between profiles:
  - Separate goals, tracker data, resources, radar snapshots, and daily plans per profile
  - Global settings (theme, font size) shared across profiles
- **Profile management**:
  - Create profiles with custom names (1-30 characters)
  - Rename profiles (display name only, folder ID stays stable)
  - Delete profiles (with safety checks against deleting active/default profile)
  - Profile selector dropdown in main window for easy switching
- **Automatic features**:
  - Remembers last active profile on startup
  - Profile name sanitization for filesystem safety
  - Orphaned folder cleanup
  - Active profile indicator (⭐) in Settings

#### ⚙️ Settings & Customization
- **Theme engine**:
  - Anki Auto mode (automatically matches Anki's light/dark theme)
  - Light Mode, Dark Mode
  - Fluency Light/Dark alternate color schemes
  - Centralized `ThemeColors` palette with consistent styling across all views
  - Real-time theme switching
- **Font size adjustment** (8pt - 24pt, default 11pt)
- **Startup behavior**: Option to open LanguageForge automatically when Anki launches
- **Profile Management UI**: Full interface for creating, renaming, and deleting profiles

---

### 🎨 Visual Design

- **Consistent theming** across all views and components
- **Interactive elements**:
  - Themed CircleIndicators with hover states
  - Styled buttons and combo boxes
  - Hoverable resource "Open" buttons
  - Themed month selectors and dropdowns
- **Card-based layout** for organized information display
- **Responsive UI** that adapts to different window sizes
- **Status bar** with timestamps for user feedback

---

### 💾 Data Management

- **Local JSON storage** in `user_data/` folder
- **Profile-aware data structure**:
  ```
  user_data/
    profiles.json          # Profile registry
    settings.json          # Global settings
    profiles/
      default/
        goals_v2.json
        tracker.json
        resources.json
        radar.json
        dailyplan.json
  ```
- **Auto-save functionality** throughout the application
- **Backward compatibility** with missing fields and future updates
- **Data isolation** ensures profile switching is safe and reliable

---

### 🏗️ Technical Highlights

- **Built with**: Python, Qt6, Anki API
- **Architecture**:
  - Modular view system (Dashboard, Tracker, Goals, Resources, Settings)
  - Centralized logic layer (`core/` modules)
  - Profile-aware storage system
  - Theme engine with dynamic color application
- **Code quality**:
  - Type hints throughout
  - Consistent naming conventions
  - Modular, maintainable structure
  - Error handling and validation

---

### 📖 Documentation

- **Comprehensive User Manual** (`USER_MANUAL.md`) included
- **Detailed feature explanations** with step-by-step instructions
- **Best practices guide** for daily, weekly, and monthly routines
- **Troubleshooting section** for common issues
- **Data backup recommendations**

---

### 🚀 Getting Started

1. Install the add-on from AnkiWeb or manually
2. Restart Anki
3. Access via **Tools → LanguageForge – Language System**
4. Start with the default profile or create your own
5. Begin tracking your language learning journey!

---

### 🙏 Thank You

Thank you for trying LanguageForge! We hope it enhances your language learning experience. Feedback and suggestions are always welcome.

**Happy language learning! 🌍📚**
