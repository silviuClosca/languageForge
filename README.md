# LanguageForge

**Version 1.0.0** | A comprehensive language learning management system for Anki

[![License: MIT (Modified)](https://img.shields.io/badge/License-MIT%20(Modified)-blue.svg)](LICENSE)

---

## 📥 Install from AnkiWeb

**Add-on code:** `[Will be added after AnkiWeb approval]`  
**AnkiWeb URL:** `[Will be added after AnkiWeb approval]`

Or install manually from source (see [Installation](#installation) below).

---

## 🎯 What is LanguageForge?

**LanguageForge** is a complete language learning management system integrated into Anki. It helps you:

- 📊 **Track daily practice** across four core skills (Reading, Listening, Speaking, Writing)
- 🎯 **Set and achieve monthly goals** with detailed subtasks and reflections
- 📚 **Organize learning resources** (books, videos, podcasts, courses)
- 🎭 **Visualize skill balance** with interactive radar charts
- 🌍 **Manage multiple languages** with separate profiles for complete data isolation
- 🎨 **Customize appearance** with themes that match Anki's light/dark modes

Perfect for serious language learners who want a centralized system to track their progress beyond just flashcard reviews.

---

## ✨ Key Features

### 📊 Dashboard – Command Center
Your overview hub showing:
- **Fluency Snapshot**: Interactive radar chart (1-5 scale) with balance index and trend arrows
- **This Week's Activity**: 4×7 grid for quick daily skill tracking
- **Daily Plan Tasks**: 4 inline editable tasks for daily planning
- **Monthly Goals Preview**: Quick view of 3 current goals with completion toggles
- **Learning Resources**: Preview of 5 recent resources with quick "Open" buttons

### 📈 Daily Tracker
- **Monthly calendar view** with all four skills displayed per day
- Visual completion circles (click to toggle)
- **Statistics**: Active days, longest streak, per-skill percentages
- Month/year navigation for historical data
- Real-time consistency tracking

### 🎯 Monthly Goals
- **3 goal slots per month** for focused objective setting
- Rich goal structure: Title, category, unlimited subtasks, reflections, timestamps
- Visual completion tracking with auto-save
- Archive system for past months (view-only)
- Categories: General, Vocabulary, Grammar, Reading, Listening, Speaking, Writing

### 📚 Learning Resources Library
- Centralized database for all learning materials
- Fields: Title, Type, URL, Status, Notes
- Types: Book, Video, Podcast, Course, Website, App, Other
- Statuses: Not Started, In Progress, Completed, Reference
- Real-time search and filtering
- One-click URL opening for online resources

### 🎭 Fluency Snapshot (Radar Chart)
- Self-assessment tool for overall language proficiency (1-5 scale per skill)
- Interactive: Drag axes to adjust values
- Ghost polygon shows previous month for comparison
- Trend arrows: ↑ improved, ↓ declined, = stable
- Balance Index (0-100%): Measures skill distribution evenness
- Monthly snapshots with full history

### 🌍 Multi-Profile System
- **Create unlimited profiles** (capped at 50 for safety) for different languages
- **Complete data isolation**: Each profile has separate goals, tracker, resources, radar, daily plans
- **Global settings**: Theme and font size shared across profiles
- **Easy switching**: Dropdown selector in main window
- **Profile management**: Create, rename, delete profiles with safety checks
- **Automatic**: Remembers last active profile on startup

### ⚙️ Settings & Customization
- **Themes**: Anki Auto (recommended), Light, Dark, Fluency Light/Dark
- **Font Size**: Adjustable from 8pt to 24pt (default: 11pt)
- **Startup Behavior**: Option to open LanguageForge automatically
- **Profile Management**: Full UI for managing language profiles

---

## 📦 Installation

### From AnkiWeb (Recommended)
1. Open Anki
2. Go to **Tools → Add-ons → Get Add-ons...**
3. Enter add-on code: `[TBD]`
4. Click **OK** and restart Anki

### From Source (Manual)
1. Download or clone this repository
2. Copy the `languageforge` folder to your Anki add-ons directory:
   - **Windows**: `%APPDATA%\Anki2\addons21\languageforge`
   - **macOS**: `~/Library/Application Support/Anki2/addons21/languageforge`
   - **Linux**: `~/.local/share/Anki2/addons21/languageforge`
3. Restart Anki
4. Open via **Tools → LanguageForge – Language System**

---

## 🚀 Quick Start

1. **First Launch**: LanguageForge opens with a "Default" profile automatically created
2. **Dashboard**: Get an overview of all features
3. **Set Goals**: Go to Goals tab and create your first monthly goal
4. **Track Daily**: Use Dashboard or Tracker tab to mark daily practice
5. **Add Resources**: Build your learning materials library in Resources tab
6. **Assess Skills**: Update your radar chart monthly to track progress
7. **Multiple Languages?** Create new profiles in Settings → Profile Management

📖 **For detailed instructions, see [USER_MANUAL.md](USER_MANUAL.md)**

---

## 💾 Data Storage & Privacy

LanguageForge stores all data **locally on your machine** in JSON files:

```
languageforge/
  user_data/
    profiles.json          # Profile registry + active profile
    settings.json          # Global settings (theme, font size)
    profiles/
      default/
        goals_v2.json      # Monthly goals
        tracker.json       # Daily activity data
        resources.json     # Learning resources
        radar.json         # Skill snapshots
        dailyplan.json     # Daily plan tasks
      spanish/             # Example profile
        [same structure]
```

### Privacy Notes
- ✅ **100% Local**: No data is sent to external servers
- ✅ **Machine-specific**: Data stays on your device
- ✅ **Git-safe**: `user_data/` is in `.gitignore`
- ✅ **Backup-friendly**: Simply copy the `user_data/` folder

### Backup Recommendations
1. Close Anki
2. Copy entire `user_data/` folder to safe location
3. Restore by replacing the folder when needed

---

## 🛠️ Development

### Requirements
- **Anki 23.10+** (Qt6-based versions)
- Python 3.9+ (bundled with Anki)
- PyQt6 (bundled with Anki)

### Project Structure

```
languageforge/
  ├── __init__.py              # Add-on entry point
  ├── main.py                  # Initialization and Anki integration
  ├── manifest.json            # Add-on metadata
  ├── gui/
  │   ├── main_window.py       # Main dockable window and tab management
  │   ├── dashboard_view.py    # Dashboard with all feature previews
  │   ├── tracker_view.py      # Monthly calendar tracker
  │   ├── goals_view.py        # Monthly goals with subtasks
  │   ├── resources_view.py    # Learning resources library
  │   ├── radar_view.py        # Radar chart and balance index
  │   ├── settings_view.py     # Settings and profile management
  │   └── widgets.py           # Shared UI components (CircleIndicator, etc.)
  ├── core/
  │   ├── storage.py           # JSON file I/O and data directory management
  │   ├── logic_profiles.py    # Multi-profile system logic
  │   ├── logic_goals.py       # Goals data logic
  │   ├── logic_tracker.py     # Tracker data logic
  │   ├── logic_resources.py   # Resources data logic
  │   ├── logic_radar.py       # Radar snapshot logic
  │   ├── logic_dailyplan.py   # Daily plan logic
  │   ├── logic_settings.py    # Settings logic
  │   ├── themes.py            # Theme colors and styling
  │   └── models.py            # Data models (dataclasses)
  └── user_data/               # User data (gitignored)
      ├── profiles.json
      ├── settings.json
      └── profiles/
          └── [profile_id]/
```

### Running From Source
1. Clone this repository
2. Copy or symlink the `languageforge` folder to your Anki `addons21` directory:
   - Windows: `%APPDATA%\Anki2\addons21\`
   - macOS: `~/Library/Application Support/Anki2/addons21/`
   - Linux: `~/.local/share/Anki2/addons21/`
3. Restart Anki
4. Access via **Tools → LanguageForge – Language System**
5. Check logs: **Tools → Add-ons → View Files** (see console output)

### Contributing
Contributions are welcome! Please:
- Follow existing code style (type hints, docstrings)
- Keep UI consistent with current design language
- Test with multiple profiles to ensure data isolation
- Update documentation if adding new features

**Areas for Contribution:**
- Translations/localization
- Additional theme options
- Export/import functionality
- Statistics visualizations
- Bug fixes and performance improvements

---

## 📚 Documentation

- **[USER_MANUAL.md](USER_MANUAL.md)** - Comprehensive user guide with step-by-step instructions
- **[RELEASE_NOTES.md](RELEASE_NOTES.md)** - Full changelog and version history
- **[LICENSE](LICENSE)** - License information

---

## 🐛 Troubleshooting

### Common Issues

**Add-on won't load:**
- Check Anki version (23.10+ required)
- Ensure folder name is exactly `languageforge`
- Check Anki console for error messages

**Data not saving:**
- Verify `user_data/` folder has write permissions
- Check available disk space
- Ensure no other process is locking files

**Profile switching not working:**
- Restart Anki to refresh profile system
- Verify `profiles.json` exists in `user_data/`
- Check that profile folders exist under `user_data/profiles/`

For more help, see the [Troubleshooting section in USER_MANUAL.md](USER_MANUAL.md#troubleshooting)

---

## 📝 License

**MIT License (Modified for Non-Commercial Use)**

You may use, modify, and distribute this software freely for **non-commercial purposes**.  
Commercial use requires obtaining a separate commercial license.

See the full [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Built with:
- **Anki** - The powerful spaced repetition system
- **Qt6/PyQt6** - Cross-platform UI framework
- **Python** - The language that powers it all

Special thanks to the Anki community and all language learners using this add-on!

---

## 📬 Contact & Support

- **Issues & Bugs**: [GitHub Issues](https://github.com/[your-username]/languageforge/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/[your-username]/languageforge/discussions)
- **AnkiWeb**: [Add-on page](https://ankiweb.net/shared/info/[code])

---

**Happy language learning! 🌍📚**

---

**Version 1.0.0** | November 2025 | Made with ❤️ for language learners


