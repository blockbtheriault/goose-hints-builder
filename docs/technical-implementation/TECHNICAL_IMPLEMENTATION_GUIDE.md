# Goose Hints Builder - Technical Implementation Guide

## 🎯 Help Menu Integration - Developer Guide

### Overview
This guide provides the technical specifications for integrating the Goose Hints Builder (Simple & Comprehensive editions) into the Goose Desktop application's Help menu.

---

## 📁 File Structure Integration

### Recommended Directory Structure:
```
goose/
├── src/
│   ├── ui/
│   │   ├── components/
│   │   │   ├── HintsBuilder/
│   │   │   │   ├── index.js                    # Main component
│   │   │   │   ├── EditionSelector.js          # Simple vs Comprehensive choice
│   │   │   │   ├── CategoryFlow.js             # Question flow interface
│   │   │   │   ├── ProgressIndicator.js        # Progress bar and navigation
│   │   │   │   ├── CompletionScreen.js         # Success and integration screen
│   │   │   │   └── styles.css                  # Component styling
│   │   │   └── Menu/
│   │   │       └── HelpMenu.js                 # Updated help menu
│   │   └── hooks/
│   │       ├── useHintsBuilder.js              # State management
│   │       └── useMemoryIntegration.js         # Goose memory integration
│   ├── services/
│   │   ├── hintsBuilder/
│   │   │   ├── categories.js                   # Category definitions
│   │   │   ├── questionFlow.js                 # Question logic
│   │   │   └── memoryService.js                # Memory persistence
│   │   └── platform/
│   │       └── platformDetection.js            # Cross-platform utilities
│   └── data/
│       └── hintsBuilder/
│           ├── simpleCategories.json           # 5-category configuration
│           └── comprehensiveCategories.json    # 13-category configuration
```

---

## 🛠️ Component Implementation

### 1. Help Menu Integration

```javascript
// src/ui/components/Menu/HelpMenu.js
import React from 'react';
import { MenuItem, SubMenu } from '@goose/ui-components';
import { HintsBuilderModal } from '../HintsBuilder';

export const HelpMenu = () => {
  const [showHintsBuilder, setShowHintsBuilder] = useState(false);
  const [selectedEdition, setSelectedEdition] = useState(null);

  const handleHintsBuilderOpen = (edition) => {
    setSelectedEdition(edition);
    setShowHintsBuilder(true);
  };

  return (
    <Menu>
      <MenuItem icon="📖" onClick={openDocumentation}>
        Documentation
      </MenuItem>
      <MenuItem icon="⌨️" onClick={showKeyboardShortcuts}>
        Keyboard Shortcuts
      </MenuItem>
      <MenuItem icon="ℹ️" onClick={showAbout}>
        About Goose
      </MenuItem>
      <MenuSeparator />
      
      <SubMenu icon="🦆" label="Goose Hints Builder">
        <MenuItem 
          icon="🚀" 
          onClick={() => handleHintsBuilderOpen('simple')}
          description="5 categories, 10-15 minutes"
        >
          Simple Setup
        </MenuItem>
        <MenuItem 
          icon="🏆" 
          onClick={() => handleHintsBuilderOpen('comprehensive')}
          description="13 categories, 20-25 minutes"
        >
          Comprehensive Setup
        </MenuItem>
      </SubMenu>
      
      <MenuItem icon="🐛" onClick={reportIssue}>
        Report Issue
      </MenuItem>

      {showHintsBuilder && (
        <HintsBuilderModal
          edition={selectedEdition}
          onClose={() => setShowHintsBuilder(false)}
          onComplete={handleHintsBuilderComplete}
        />
      )}
    </Menu>
  );
};
```

### 2. Main Hints Builder Component

```javascript
// src/ui/components/HintsBuilder/index.js
import React, { useState, useEffect } from 'react';
import { Modal } from '@goose/ui-components';
import { useHintsBuilder } from '../../hooks/useHintsBuilder';
import { useMemoryIntegration } from '../../hooks/useMemoryIntegration';
import { EditionSelector } from './EditionSelector';
import { CategoryFlow } from './CategoryFlow';
import { CompletionScreen } from './CompletionScreen';

export const HintsBuilderModal = ({ edition, onClose, onComplete }) => {
  const {
    currentStep,
    categories,
    preferences,
    progress,
    nextCategory,
    previousCategory,
    setPreference,
    switchEdition,
    isComplete
  } = useHintsBuilder(edition);

  const { saveToMemory, isLoading } = useMemoryIntegration();

  const handleComplete = async () => {
    try {
      await saveToMemory(preferences, edition);
      onComplete(preferences);
      onClose();
    } catch (error) {
      console.error('Failed to save preferences:', error);
      // Handle error appropriately
    }
  };

  const renderCurrentStep = () => {
    switch (currentStep) {
      case 'edition-select':
        return (
          <EditionSelector
            onSelect={switchEdition}
            onCancel={onClose}
          />
        );
      case 'category-flow':
        return (
          <CategoryFlow
            categories={categories}
            preferences={preferences}
            progress={progress}
            onSetPreference={setPreference}
            onNext={nextCategory}
            onPrevious={previousCategory}
            onSwitchEdition={switchEdition}
            onCancel={onClose}
          />
        );
      case 'completion':
        return (
          <CompletionScreen
            edition={edition}
            preferences={preferences}
            onComplete={handleComplete}
            onCancel={onClose}
            isLoading={isLoading}
          />
        );
      default:
        return null;
    }
  };

  return (
    <Modal
      isOpen={true}
      onClose={onClose}
      size="large"
      title="🦆 Goose Hints Builder"
    >
      {renderCurrentStep()}
    </Modal>
  );
};
```

### 3. State Management Hook

```javascript
// src/ui/hooks/useHintsBuilder.js
import { useState, useEffect } from 'react';
import { getCategories } from '../../services/hintsBuilder/categories';

export const useHintsBuilder = (initialEdition = null) => {
  const [edition, setEdition] = useState(initialEdition);
  const [currentStep, setCurrentStep] = useState(
    initialEdition ? 'category-flow' : 'edition-select'
  );
  const [currentCategoryIndex, setCurrentCategoryIndex] = useState(0);
  const [preferences, setPreferences] = useState({});
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    if (edition) {
      const categoryList = getCategories(edition);
      setCategories(categoryList);
      setCurrentStep('category-flow');
    }
  }, [edition]);

  const progress = {
    current: currentCategoryIndex + 1,
    total: categories.length,
    percentage: ((currentCategoryIndex + 1) / categories.length) * 100
  };

  const switchEdition = (newEdition) => {
    setEdition(newEdition);
    setCurrentCategoryIndex(0);
    setPreferences({});
  };

  const setPreference = (categoryKey, preference) => {
    setPreferences(prev => ({
      ...prev,
      [categoryKey]: preference
    }));
  };

  const nextCategory = () => {
    if (currentCategoryIndex < categories.length - 1) {
      setCurrentCategoryIndex(prev => prev + 1);
    } else {
      setCurrentStep('completion');
    }
  };

  const previousCategory = () => {
    if (currentCategoryIndex > 0) {
      setCurrentCategoryIndex(prev => prev - 1);
    }
  };

  const isComplete = currentStep === 'completion';

  return {
    edition,
    currentStep,
    categories,
    currentCategory: categories[currentCategoryIndex],
    preferences,
    progress,
    nextCategory,
    previousCategory,
    setPreference,
    switchEdition,
    isComplete
  };
};
```

### 4. Memory Integration Service

```javascript
// src/ui/hooks/useMemoryIntegration.js
import { useState } from 'react';
import { memoryService } from '../../services/hintsBuilder/memoryService';

export const useMemoryIntegration = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const saveToMemory = async (preferences, edition) => {
    setIsLoading(true);
    setError(null);

    try {
      // Save edition metadata
      await memoryService.remember({
        category: 'user_preferences_meta',
        data: `Goose Hints Builder ${edition} Edition completed on ${new Date().toISOString()}`,
        is_global: true,
        tags: ['hints_builder', 'meta', edition]
      });

      // Save individual preferences
      for (const [category, preference] of Object.entries(preferences)) {
        await memoryService.remember({
          category: `user_preferences_${category}`,
          data: preference.hint,
          is_global: true,
          tags: ['hints_builder', 'personalization', category, edition]
        });
      }

      // Trigger Goose to reload preferences
      await memoryService.activatePreferences();

    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    saveToMemory,
    isLoading,
    error
  };
};
```

### 5. Category Definitions

```javascript
// src/services/hintsBuilder/categories.js
import simpleCategories from '../../data/hintsBuilder/simpleCategories.json';
import comprehensiveCategories from '../../data/hintsBuilder/comprehensiveCategories.json';

export const getCategories = (edition) => {
  switch (edition) {
    case 'simple':
      return simpleCategories;
    case 'comprehensive':
      return comprehensiveCategories;
    default:
      return [];
  }
};

export const getCategoryCount = (edition) => {
  return getCategories(edition).length;
};

export const getEstimatedTime = (edition) => {
  switch (edition) {
    case 'simple':
      return '10-15 minutes';
    case 'comprehensive':
      return '20-25 minutes';
    default:
      return 'Unknown';
  }
};
```

---

## 📄 Configuration Files

### Simple Categories Configuration:
```json
// src/data/hintsBuilder/simpleCategories.json
[
  {
    "key": "output_formats",
    "title": "Output Formats",
    "description": "When I analyze data and show you results, which format feels most useful?",
    "options": [
      {
        "key": "markdown_tables",
        "label": "Clean markdown tables with summaries",
        "hint": "Present data in well-formatted markdown tables with executive summaries"
      },
      {
        "key": "mixed_approach",
        "label": "Mix of tables, charts, and summaries",
        "hint": "Use varied presentation formats: tables, charts, and executive summaries"
      },
      {
        "key": "visual_charts",
        "label": "Charts and visualizations when possible",
        "hint": "Create visualizations and charts for data presentation"
      }
    ],
    "allowCustom": true
  },
  {
    "key": "communication_style",
    "title": "Communication Style",
    "description": "How would you like me to communicate during tasks?",
    "options": [
      {
        "key": "detailed_progress",
        "label": "Show me detailed progress and steps",
        "hint": "Display all working steps and execution progress with full transparency"
      },
      {
        "key": "milestone_updates",
        "label": "Update me at key milestones only",
        "hint": "Provide updates at key milestones during longer tasks"
      }
    ],
    "allowCustom": true
  }
  // ... additional categories
]
```

---

## 🔧 Platform Integration

### Platform Detection Service:
```javascript
// src/services/platform/platformDetection.js
export const getPlatformInfo = () => {
  const platform = window.navigator.platform;
  const userAgent = window.navigator.userAgent;
  
  let system = 'Unknown';
  if (platform.includes('Win')) system = 'Windows';
  else if (platform.includes('Mac')) system = 'Darwin';
  else if (platform.includes('Linux')) system = 'Linux';
  
  // Get platform-appropriate default paths
  const getDefaultPaths = () => {
    const homeDir = window.electron?.getHomePath() || '~';
    
    switch (system) {
      case 'Windows':
        return {
          projects: `${homeDir}\\Documents\\Projects`,
          desktop: `${homeDir}\\Desktop`,
          documents: `${homeDir}\\Documents`
        };
      default:
        return {
          projects: `${homeDir}/Projects`,
          desktop: `${homeDir}/Desktop`,
          documents: `${homeDir}/Documents`
        };
    }
  };

  return {
    system,
    platform,
    userAgent,
    paths: getDefaultPaths()
  };
};
```

---

## 🎨 Styling Integration

### Component Styles:
```css
/* src/ui/components/HintsBuilder/styles.css */
.hints-builder-modal {
  --primary-color: var(--goose-primary);
  --secondary-color: var(--goose-secondary);
  --background-color: var(--goose-background);
  --text-color: var(--goose-text);
  --border-color: var(--goose-border);
}

.edition-selector {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 2rem;
}

.edition-card {
  border: 2px solid var(--border-color);
  border-radius: 8px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.edition-card:hover {
  border-color: var(--primary-color);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.edition-card.selected {
  border-color: var(--primary-color);
  background-color: var(--primary-color-light);
}

.progress-indicator {
  width: 100%;
  height: 8px;
  background-color: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: var(--primary-color);
  transition: width 0.3s ease;
}

.category-options {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin: 1.5rem 0;
}

.option-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.option-item:hover {
  background-color: var(--background-color-light);
  border-color: var(--primary-color);
}

.option-item.selected {
  background-color: var(--primary-color-light);
  border-color: var(--primary-color);
}
```

---

## 🚀 Deployment Checklist

### Pre-Implementation:
- [ ] Review existing Goose UI component library
- [ ] Confirm memory service API compatibility
- [ ] Validate platform detection requirements
- [ ] Test modal/dialog integration patterns

### Implementation Phase 1:
- [ ] Add Help menu items for both editions
- [ ] Create basic modal with edition selection
- [ ] Implement Simple edition (5 categories)
- [ ] Basic memory integration
- [ ] Platform detection service

### Implementation Phase 2:
- [ ] Add Comprehensive edition (13 categories)
- [ ] Enhanced UI with progress indicators
- [ ] Custom preference handling
- [ ] Edition switching capability
- [ ] Export/import functionality

### Testing & Validation:
- [ ] Cross-platform testing (Windows, macOS, Linux)
- [ ] Memory persistence validation
- [ ] UI responsiveness testing
- [ ] Accessibility compliance
- [ ] Performance optimization

### Documentation:
- [ ] User documentation for Help menu access
- [ ] Developer documentation for extensions
- [ ] Configuration guide for organizations
- [ ] Troubleshooting guide

---

## 🎯 Success Metrics

### User Adoption:
- Help menu click-through rates
- Edition selection preferences
- Completion rates by edition
- User satisfaction scores

### Technical Performance:
- Modal load times
- Memory integration success rates
- Cross-platform compatibility
- Error rates and recovery

### Business Impact:
- User engagement improvement
- Support ticket reduction
- Enterprise adoption rates
- Community feedback scores

---

This technical implementation guide provides everything needed to integrate the Goose Hints Builder into the Help menu with both Simple and Comprehensive editions! 🦆🚀
