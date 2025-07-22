# 🦆 Goose Hints Builder

A universal preference discovery system that personalizes the Goose AI assistant for individual workflows. Built with cross-platform compatibility and designed for seamless integration into Goose's Help menu.

[![Platform Support](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](#platform-support)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](#requirements)
[![License](https://img.shields.io/badge/license-MIT-green)](#license)
[![Goose Integration](https://img.shields.io/badge/goose-help%20menu%20ready-orange)](#help-menu-integration)

## 🎯 Overview

The **Goose Hints Builder** transforms how users personalize their AI assistant experience. Instead of manually configuring preferences, users go through an intuitive conversation that discovers their workflow preferences and automatically generates personalized hints for Goose.

### ✨ Key Features

- **🚀 Two Editions**: Simple (5 categories, 10-15 min) and Comprehensive (13 categories, 20-25 min)
- **🌍 Universal Compatibility**: Works on Windows, macOS, and Linux
- **☁️ Multiple Cloud Options**: Google Drive, OneDrive, Dropbox, iCloud, and custom providers
- **🎛️ Custom Preferences**: "Something else" option for every category
- **🔗 Memory Integration**: Direct integration with Goose's memory system
- **🎨 Help Menu Ready**: Complete UI specifications for native Goose integration

## 🚀 Quick Start

### Simple Edition (10-15 minutes)
```bash
python3 src/goose_hints_builder_simple.py
```

### Comprehensive Edition (20-25 minutes)
```bash
python3 src/goose_hints_builder_comprehensive.py
```

### Demo Mode
```bash
python3 examples/demo_interactive_experience.py
```

### Compatibility Test
```bash
python3 tests/test_universal_compatibility.py
```

## 📋 Categories Covered

### 🚀 Simple Edition (5 Categories)
1. **Output Formats** - How you want data and results presented
2. **Communication Style** - How you want Goose to communicate during tasks
3. **File Management** - Directory structure, cloud storage, and organization
4. **Document Formatting** - Fonts, document types, and formatting preferences
5. **Coding Preferences** - Programming language preferences and development approach

### 🏆 Comprehensive Edition (13 Categories)
All Simple categories **PLUS**:
6. **Documentation Standards** - Comments, README files, code documentation
7. **Data Analysis Approach** - Technical depth vs business insights
8. **Feedback & Learning** - How to handle corrections and improvements
9. **Progress Reporting** - Detailed updates vs silent execution
10. **Decision Making** - Autonomy levels and approval requirements
11. **Time Management** - Prioritization and task sequencing
12. **Error Handling** - Debugging detail and error recovery
13. **Workflow Patterns** - Sequential vs parallel, automation preferences
14. **Security & Privacy** - Data handling and sharing preferences

## 🛠️ Installation

### Requirements
- Python 3.7 or higher
- Cross-platform compatibility (Windows, macOS, Linux)

### Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/goose-hints-builder.git
cd goose-hints-builder

# No additional dependencies required - uses Python standard library only
```

## 📁 Project Structure

```
goose-hints-builder/
├── src/                                    # Source code
│   ├── goose_hints_builder_simple.py      # Simple Edition (5 categories)
│   └── goose_hints_builder_comprehensive.py # Comprehensive Edition (13 categories)
├── examples/                               # Demo and examples
│   └── demo_interactive_experience.py     # Interactive demo
├── tests/                                  # Testing and validation
│   └── test_universal_compatibility.py    # Cross-platform tests
├── docs/                                   # Documentation
│   ├── help-menu-integration/             # Help menu integration specs
│   ├── technical-implementation/          # Developer guides
│   └── user-guides/                       # User documentation
├── .github/                                # GitHub configuration
│   ├── workflows/                          # CI/CD workflows
│   └── ISSUE_TEMPLATE/                     # Issue templates
├── README.md                               # This file
├── LICENSE                                 # MIT License
├── CONTRIBUTING.md                         # Contribution guidelines
└── CHANGELOG.md                            # Version history
```

## 🎯 Help Menu Integration

The Goose Hints Builder is designed for seamless integration into Goose's Help menu:

```
Help
├── Documentation
├── Keyboard Shortcuts  
├── About Goose
├── ─────────────────
├── 🦆 Goose Hints Builder    ← NEW SUBMENU
│   ├── 🚀 Simple Setup (5 categories, 10-15 min)
│   └── 🏆 Comprehensive Setup (13 categories, 20-25 min)
└── Report Issue
```

See [`docs/help-menu-integration/`](docs/help-menu-integration/) for complete implementation specifications.

## 🌍 Platform Support

### Tested Platforms
- ✅ **macOS** (Darwin) - Primary development platform
- ✅ **Windows** - Universal file path handling
- ✅ **Linux** - Cross-platform compatibility validated

### Cloud Storage Support
- ✅ **Google Drive** - Primary integration
- ✅ **Microsoft OneDrive** - Enterprise support
- ✅ **Dropbox** - Universal compatibility
- ✅ **iCloud Drive** - macOS integration
- ✅ **Custom Providers** - Flexible configuration

## 🧪 Testing

Run the compatibility test to validate on your platform:

```bash
python3 tests/test_universal_compatibility.py
```

Expected output:
```
🚀 UNIVERSAL GOOSE HINTS BUILDER - VALIDATION COMPLETE
✅ Cross-platform compatibility: PASSED
✅ Universal file paths: PASSED
✅ Multiple cloud options: PASSED
✅ Platform detection: PASSED
✅ No user-specific assumptions: PASSED
```

## 📖 Documentation

- **[User Guides](docs/user-guides/)** - How to use both editions
- **[Technical Implementation](docs/technical-implementation/)** - Developer integration guide
- **[Help Menu Integration](docs/help-menu-integration/)** - UI specifications and mockups
- **[API Documentation](docs/api/)** - Memory integration and extension points

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/goose-hints-builder.git
cd goose-hints-builder

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes and test
python3 tests/test_universal_compatibility.py

# Commit and push
git commit -m "Add your feature"
git push origin feature/your-feature-name

# Create a Pull Request
```

## 🎯 Roadmap

### Phase 1: Core Integration ✅
- [x] Simple and Comprehensive editions
- [x] Universal platform compatibility
- [x] Memory system integration
- [x] Help menu specifications

### Phase 2: Enhanced Features 🚧
- [ ] React component implementation
- [ ] Rich visual interface
- [ ] Template import/export
- [ ] Team sharing capabilities

### Phase 3: Enterprise Features 📋
- [ ] Organization-wide defaults
- [ ] Bulk deployment tools
- [ ] Template marketplace
- [ ] Advanced customization

### Phase 4: Community Features 🌟
- [ ] Community-contributed presets
- [ ] Plugin architecture
- [ ] Third-party integrations
- [ ] Analytics and insights

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Block/Goose Team** - For creating an amazing AI assistant platform
- **Open Source Community** - For inspiration and best practices
- **Contributors** - For making this project better

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/goose-hints-builder/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/goose-hints-builder/discussions)
- **Documentation**: [Project Docs](docs/)

---

**Ready to personalize your Goose experience? Start with the Simple Edition and upgrade to Comprehensive when you're ready for more control!** 🦆✨
