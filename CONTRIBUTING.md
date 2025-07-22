# Contributing to Goose Hints Builder

Thank you for your interest in contributing to the Goose Hints Builder! This document provides guidelines and information for contributors.

## 🎯 Project Vision

The Goose Hints Builder aims to make AI assistant personalization accessible to everyone through:
- Universal cross-platform compatibility
- Intuitive user experience
- Professional-grade configuration
- Seamless Goose integration

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Git for version control
- Basic understanding of Python and CLI tools

### Development Setup
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/goose-hints-builder.git
cd goose-hints-builder

# Create a feature branch
git checkout -b feature/your-feature-name

# Test the existing functionality
python3 tests/test_universal_compatibility.py
```

## 📋 How to Contribute

### 1. Types of Contributions

#### 🐛 Bug Reports
- Use the bug report template in Issues
- Include platform information (OS, Python version)
- Provide steps to reproduce
- Include expected vs actual behavior

#### ✨ Feature Requests
- Use the feature request template in Issues
- Explain the use case and benefit
- Consider backward compatibility
- Discuss implementation approach

#### 💻 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Documentation updates
- Test coverage improvements

#### 📖 Documentation
- User guides and tutorials
- API documentation
- Code comments and docstrings
- README improvements

### 2. Development Workflow

#### Branch Naming
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `test/description` - Test improvements

#### Commit Messages
Follow conventional commits format:
```
type(scope): description

Examples:
feat(simple): add custom preference validation
fix(comprehensive): resolve platform detection issue
docs(readme): update installation instructions
test(compatibility): add Windows path validation
```

#### Pull Request Process
1. **Create a feature branch** from `main`
2. **Make your changes** with clear, focused commits
3. **Test thoroughly** on your platform
4. **Update documentation** if needed
5. **Submit a pull request** with:
   - Clear description of changes
   - Reference to related issues
   - Testing performed
   - Screenshots if UI changes

## 🧪 Testing Guidelines

### Running Tests
```bash
# Run compatibility tests
python3 tests/test_universal_compatibility.py

# Test Simple Edition
python3 src/goose_hints_builder_simple.py

# Test Comprehensive Edition  
python3 src/goose_hints_builder_comprehensive.py

# Run demo
python3 examples/demo_interactive_experience.py
```

### Test Coverage
- All new features must include tests
- Bug fixes should include regression tests
- Platform-specific code needs cross-platform testing
- Memory integration requires validation tests

### Platform Testing
Test on multiple platforms when possible:
- **Windows**: File path handling, directory creation
- **macOS**: Default paths, iCloud integration
- **Linux**: Universal compatibility, package management

## 📝 Code Style Guidelines

### Python Code Style
- Follow PEP 8 style guide
- Use descriptive variable and function names
- Include docstrings for all functions
- Keep functions focused and single-purpose
- Use type hints where appropriate

### Documentation Style
- Use clear, concise language
- Include code examples
- Maintain consistent formatting
- Update README for significant changes

### Example Code Structure
```python
def ask_user_preference(question: str, options: list, category_info: dict) -> dict:
    """
    Ask user for preference with universal compatibility.
    
    Args:
        question: The question to ask the user
        options: List of available options
        category_info: Category metadata
        
    Returns:
        Selected preference with hint and metadata
        
    Raises:
        KeyboardInterrupt: If user cancels the process
    """
    # Implementation here
```

## 🎯 Specific Contribution Areas

### 1. Platform Compatibility
- Test on different operating systems
- Improve file path handling
- Add cloud storage providers
- Enhance platform detection

### 2. User Experience
- Improve question flow
- Add better error messages
- Enhance progress indicators
- Create better help text

### 3. Goose Integration
- Memory system improvements
- Help menu implementation
- React component development
- API integration

### 4. Enterprise Features
- Team sharing capabilities
- Organization defaults
- Bulk deployment tools
- Template marketplace

## 🔍 Code Review Process

### Review Criteria
- **Functionality**: Does it work as intended?
- **Compatibility**: Works across platforms?
- **Code Quality**: Clean, readable, maintainable?
- **Testing**: Adequate test coverage?
- **Documentation**: Clear and complete?
- **Performance**: Efficient implementation?

### Review Timeline
- Initial review within 48 hours
- Follow-up responses within 24 hours
- Approval requires 2 maintainer reviews
- Merge after all checks pass

## 🚀 Release Process

### Version Numbering
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes, backward compatible

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped
- [ ] GitHub release created
- [ ] Integration tests completed

## 📞 Getting Help

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community discussion
- **Pull Request Comments**: Code-specific discussions

### Maintainer Response Time
- Issues: Within 48 hours
- Pull Requests: Within 24 hours
- Discussions: Within 72 hours

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments
- CHANGELOG.md for each release
- GitHub contributors page
- Special mentions for significant contributions

## 📋 Issue Templates

Use the provided templates for:
- Bug reports
- Feature requests
- Documentation improvements
- Performance issues

## 🎉 Thank You!

Every contribution, no matter how small, helps make the Goose Hints Builder better for everyone. We appreciate your time and effort in improving this project!

---

**Questions?** Feel free to open a discussion or reach out to the maintainers. We're here to help! 🦆✨
