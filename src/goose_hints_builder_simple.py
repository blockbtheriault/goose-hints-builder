#!/usr/bin/env python3
"""
Goose Hints Builder - Simple Version
A streamlined, platform-agnostic preference discovery system for personalizing Goose AI assistant.
Quick 5-category setup (10-15 minutes) covering essential preferences.
Designed to work across different operating systems, cloud providers, and user setups.
"""

import json
import os
import platform
from datetime import datetime
from pathlib import Path

def get_user_platform_info():
    """Get platform-specific information for better defaults"""
    system = platform.system()
    home_dir = Path.home()
    
    # Platform-specific defaults
    if system == "Windows":
        default_projects = home_dir / "Documents" / "Projects"
        default_desktop = home_dir / "Desktop"
        default_documents = home_dir / "Documents"
    else:  # macOS, Linux, Unix
        default_projects = home_dir / "Projects"
        default_desktop = home_dir / "Desktop" 
        default_documents = home_dir / "Documents"
    
    return {
        "system": system,
        "home": home_dir,
        "projects": default_projects,
        "desktop": default_desktop,
        "documents": default_documents
    }

def get_universal_user_choice(question, options, category_num, total_categories, allow_custom=True):
    """Universal user choice with custom options and category tracking"""
    while True:
        print(f"\n🎯 **Category {category_num} of {total_categories}**")
        print(f"\n📋 **{question}**")
        print("\nOptions:")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option['label']}")
        
        if allow_custom:
            print(f"  {len(options) + 1}. Something else (I'll specify my own preference)")
        
        max_choice = len(options) + (1 if allow_custom else 0)
        prompt = f"\n👤 Choose 1-{max_choice} (or 'explain' for details): "
        
        try:
            response = input(prompt).strip().lower()
            
            if response == 'explain':
                print("\n🦆 Here's what each option means:")
                for i, option in enumerate(options, 1):
                    print(f"  {i}. {option['label']}")
                    print(f"     → This would make me: {option['hint']}")
                if allow_custom:
                    print(f"  {len(options) + 1}. Something else")
                    print(f"     → You can specify your own custom preference")
                continue
            
            choice_num = int(response)
            if 1 <= choice_num <= len(options):
                chosen_option = options[choice_num - 1]
                print(f"\n✅ Got it! I'll {chosen_option['hint'].lower()}")
                return chosen_option
            elif allow_custom and choice_num == len(options) + 1:
                return handle_custom_preference(question)
            else:
                print(f"Please choose a number between 1 and {max_choice}")
                
        except ValueError:
            print("Please enter a number or 'explain'")
        except KeyboardInterrupt:
            print("\n\n👋 Setup cancelled. You can run this anytime!")
            return None

def handle_custom_preference(question):
    """Handle custom user preferences"""
    print(f"\n💭 **Custom Preference for:** {question}")
    print("Please describe how you'd like me to handle this:")
    
    try:
        custom_response = input("\n👤 Your preference: ").strip()
        if not custom_response:
            print("Please provide a preference description.")
            return handle_custom_preference(question)
        
        # Ask for clarification if needed
        print(f"\n🤔 To make sure I understand correctly:")
        print(f"You want me to: {custom_response}")
        
        confirm = input("\n👤 Is this correct? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y', 'correct', 'right']:
            custom_option = {
                'key': 'custom_preference',
                'label': f"Custom: {custom_response}",
                'hint': custom_response
            }
            print(f"\n✅ Perfect! I'll {custom_response.lower()}")
            return custom_option
        else:
            print("Let's try again...")
            return handle_custom_preference(question)
            
    except KeyboardInterrupt:
        print("\n\n👋 Returning to main options...")
        return None

def ask_for_document_preferences():
    """Ask for document and formatting preferences - platform agnostic"""
    print("\n📄 **Document Formatting Preferences**")
    print("Let's set up your document and formatting preferences.")
    
    preferences = {}
    
    # Ask about exemplar files
    print("\n📋 **Do you have any exemplar files that show your preferred formatting style?**")
    print("(These help me understand your document layout, style, and structure preferences)")
    print("Examples: /path/to/report.docx, ~/Documents/template.md, C:\\Templates\\format.pdf")
    
    exemplar_response = input("\n👤 File paths (comma-separated) or 'none': ").strip()
    
    if exemplar_response.lower() not in ['none', 'no', '']:
        preferences['exemplar_files'] = exemplar_response
        print(f"✅ I'll reference these files for formatting style: {exemplar_response}")
    else:
        print("✅ No exemplar files - I'll use standard professional formatting")
    
    # Ask about preferred fonts
    print("\n📋 **What's your preferred font for documents?**")
    font_options = [
        {"key": "montserrat", "label": "Montserrat (modern, clean)", "hint": "Use Montserrat as primary font"},
        {"key": "roboto", "label": "Roboto (readable, professional)", "hint": "Use Roboto as primary font"},
        {"key": "arial", "label": "Arial (classic, universal)", "hint": "Use Arial as primary font"},
        {"key": "times", "label": "Times New Roman (traditional, formal)", "hint": "Use Times New Roman as primary font"},
        {"key": "system_default", "label": "System default font", "hint": "Use system default font for documents"}
    ]
    
    font_choice = get_universal_user_choice(
        "What's your preferred font for documents?", 
        font_options, 
        "Font", "Preferences", 
        allow_custom=True
    )
    
    if font_choice:
        preferences['preferred_font'] = font_choice
    
    # Ask about document storage type - multiple cloud options
    print("\n📋 **What's your preferred document format for final deliverables?**")
    format_options = [
        {"key": "cloud_docs", "label": "Cloud documents (Google Docs, Office 365, etc.)", "hint": "Create documents in cloud-based collaborative format"},
        {"key": "markdown", "label": "Markdown (portable, version-controllable)", "hint": "Create documents in Markdown format"},
        {"key": "pdf", "label": "PDF (professional, print-ready)", "hint": "Create documents in PDF format"},
        {"key": "word", "label": "Microsoft Word (standard business format)", "hint": "Create documents in Word format"},
        {"key": "plain_text", "label": "Plain text (simple, universal)", "hint": "Create documents in plain text format"}
    ]
    
    format_choice = get_universal_user_choice(
        "What's your preferred document format for final deliverables?",
        format_options,
        "Format", "Preferences",
        allow_custom=True
    )
    
    if format_choice:
        preferences['document_format'] = format_choice
    
    return preferences

def ask_universal_file_management(category_num, total_categories):
    """Universal file management with cross-platform support"""
    print(f"\n🎯 **Category {category_num} of {total_categories}: File Management**")
    print("Let's set up comprehensive file organization preferences.")
    
    platform_info = get_user_platform_info()
    preferences = {}
    
    # Root directory preferences - platform aware
    print("\n📋 **What should be your default root directory for projects?**")
    root_options = [
        {"key": "home_projects", "label": f"Projects folder ({platform_info['projects']})", "hint": f"Use {platform_info['projects']} as root with project subdirectories"},
        {"key": "desktop", "label": f"Desktop ({platform_info['desktop']})", "hint": "Use Desktop as primary working directory"},
        {"key": "documents", "label": f"Documents folder ({platform_info['documents']})", "hint": "Use Documents folder as root directory"},
        {"key": "current_dir", "label": "Current working directory", "hint": "Use current directory as project root"},
        {"key": "custom_path", "label": "Custom path (I'll specify)", "hint": "Use custom specified root directory"}
    ]
    
    root_choice = get_universal_user_choice(
        "What should be your default root directory for projects?",
        root_options,
        category_num, total_categories,
        allow_custom=True
    )
    
    if root_choice and root_choice['key'] == 'custom_path':
        custom_path = input(f"\n👤 Enter your preferred root directory path: ").strip()
        # Validate path exists or can be created
        try:
            Path(custom_path).mkdir(parents=True, exist_ok=True)
            root_choice['hint'] = f"Use {custom_path} as root directory"
            print(f"✅ I'll use {custom_path} as your root directory")
        except Exception as e:
            print(f"⚠️  Warning: Could not validate path {custom_path}: {e}")
            print("I'll still use this path, but please ensure it's accessible")
            root_choice['hint'] = f"Use {custom_path} as root directory"
    
    preferences['root_directory'] = root_choice
    
    # Data organization structure
    print("\n📋 **How should I organize project data and files?**")
    org_options = [
        {"key": "cookiecutter", "label": "Data science structure (data/, src/, docs/, notebooks/)", "hint": "Use cookiecutter data science project structure"},
        {"key": "simple_folders", "label": "Simple folders (input/, output/, scripts/)", "hint": "Use simple three-folder organization structure"},
        {"key": "by_date", "label": "Date-based organization (YYYY-MM-DD folders)", "hint": "Organize files chronologically by date"},
        {"key": "by_type", "label": "File type organization (csv/, scripts/, reports/)", "hint": "Organize files by type and format"},
        {"key": "flat_structure", "label": "Flat structure (all files in project root)", "hint": "Keep all project files in single directory"}
    ]
    
    org_choice = get_universal_user_choice(
        "How should I organize project data and files?",
        org_options,
        category_num, total_categories,
        allow_custom=True
    )
    
    preferences['data_organization'] = org_choice
    
    # Cloud backup preferences - multiple providers
    print("\n📋 **Should I automatically create backups in cloud storage?**")
    backup_options = [
        {"key": "always_backup", "label": "Yes, backup all important files automatically", "hint": "Automatically backup important files to your preferred cloud storage"},
        {"key": "ask_for_backup", "label": "Ask me for each important file", "hint": "Confirm before backing up files to cloud storage"},
        {"key": "manual_backup", "label": "No automatic backups, I'll handle it manually", "hint": "No automatic cloud backups"},
        {"key": "selective_backup", "label": "Only backup final deliverables and reports", "hint": "Backup only completed work and final outputs to cloud storage"},
        {"key": "local_backup", "label": "Local backups only (no cloud)", "hint": "Create local backup copies without cloud storage"}
    ]
    
    backup_choice = get_universal_user_choice(
        "Should I automatically create backups in cloud storage?",
        backup_options,
        category_num, total_categories,
        allow_custom=True
    )
    
    preferences['backup_strategy'] = backup_choice
    
    # If they want cloud backup, ask about preferred provider
    if backup_choice and backup_choice['key'] in ['always_backup', 'ask_for_backup', 'selective_backup']:
        print("\n📋 **Which cloud storage do you prefer?**")
        cloud_options = [
            {"key": "google_drive", "label": "Google Drive", "hint": "Use Google Drive for cloud backups"},
            {"key": "onedrive", "label": "Microsoft OneDrive", "hint": "Use OneDrive for cloud backups"},
            {"key": "dropbox", "label": "Dropbox", "hint": "Use Dropbox for cloud backups"},
            {"key": "icloud", "label": "iCloud Drive (macOS)", "hint": "Use iCloud Drive for cloud backups"},
            {"key": "multiple", "label": "Multiple providers", "hint": "Use multiple cloud storage providers"},
        ]
        
        cloud_choice = get_universal_user_choice(
            "Which cloud storage do you prefer?",
            cloud_options,
            "Cloud", "Storage",
            allow_custom=True
        )
        
        preferences['cloud_provider'] = cloud_choice
    
    return preferences

def ask_communication_style(category_num, total_categories):
    """Ask about communication and interaction preferences"""
    print(f"\n🎯 **Category {category_num} of {total_categories}: Communication Style**")
    
    options = [
        {"key": "detailed_progress", "label": "Show me detailed progress and steps", "hint": "Display all working steps and execution progress with full transparency"},
        {"key": "silent_execution", "label": "Work quietly, show me final results", "hint": "Execute tasks silently and present final results without progress updates"},
        {"key": "milestone_updates", "label": "Update me at key milestones only", "hint": "Provide updates at key milestones during longer tasks"},
        {"key": "interactive", "label": "Ask me questions and confirm decisions", "hint": "Seek confirmation for decisions and ask clarifying questions regularly"}
    ]
    
    choice = get_universal_user_choice(
        "How would you like me to communicate during tasks?",
        options, category_num, total_categories
    )
    
    return {'communication_style': choice}

def ask_output_formats(category_num, total_categories):
    """Ask about preferred output formats"""
    print(f"\n🎯 **Category {category_num} of {total_categories}: Output Formats**")
    
    options = [
        {"key": "markdown_tables", "label": "Clean markdown tables with summaries", "hint": "Present data in well-formatted markdown tables with executive summaries"},
        {"key": "code_output", "label": "Raw code output with technical details", "hint": "Show detailed technical output with code execution details"},
        {"key": "visual_charts", "label": "Charts and visualizations when possible", "hint": "Create visualizations and charts for data presentation"},
        {"key": "mixed_approach", "label": "Mix of tables, charts, and summaries", "hint": "Use varied presentation formats: tables, charts, and executive summaries"},
        {"key": "simple_text", "label": "Simple text responses", "hint": "Provide clear, simple text responses without complex formatting"}
    ]
    
    choice = get_universal_user_choice(
        "When I analyze data and show you results, which format feels most useful?", 
        options, category_num, total_categories
    )
    
    return {'output_formats': choice}

def ask_coding_preferences(category_num, total_categories):
    """Ask about coding and development preferences"""
    print(f"\n🎯 **Category {category_num} of {total_categories}: Coding Preferences**")
    
    options = [
        {"key": "python_focus", "label": "Python for most programming tasks", "hint": "Prefer Python for data analysis and programming tasks"},
        {"key": "r_focus", "label": "R for data analysis, Python for other tasks", "hint": "Prefer R for data analysis and Python for other programming tasks"},
        {"key": "javascript_focus", "label": "JavaScript for web and automation tasks", "hint": "Prefer JavaScript for web development and automation"},
        {"key": "language_agnostic", "label": "Choose best language for each task", "hint": "Select the most appropriate programming language for each specific task"},
        {"key": "minimal_code", "label": "Minimize coding, prefer existing tools", "hint": "Use existing tools and minimize custom code development"}
    ]
    
    choice = get_universal_user_choice(
        "What are your programming language preferences?",
        options, category_num, total_categories
    )
    
    return {'coding_preferences': choice}

def universal_hints_builder():
    """Run universal hints builder for all platforms and users"""
    
    platform_info = get_user_platform_info()
    
    print("🦆 **Goose Hints Builder - Simple Edition**")
    print("="*60)
    print(f"\nDetected system: {platform_info['system']}")
    print(f"Home directory: {platform_info['home']}")
    print("\nHi! I'm your universal Goose Hints Builder.")
    print("This tool works across all platforms and personalizes Goose for YOUR workflow.")
    print("\n✅ Platform-agnostic (Windows, macOS, Linux)")
    print("✅ Multiple cloud storage options")
    print("✅ Custom preferences for any category")
    print("✅ Universal file path handling")
    print("\nThis will take about 10-15 minutes for a completely personalized experience.")
    
    # Ask if user wants to proceed
    start_response = input("\n👤 Ready to build your personalized Goose hints? (yes/no): ").strip().lower()
    
    if start_response not in ['yes', 'y', 'sure', 'ok', 'ready']:
        print("\n👋 No problem! You can run this hints builder anytime.")
        return None, None
    
    preferences = {}
    total_categories = 5  # Streamlined for universal use
    
    # CATEGORY 1: OUTPUT FORMATS
    output_prefs = ask_output_formats(1, total_categories)
    preferences.update(output_prefs)
    
    # CATEGORY 2: COMMUNICATION STYLE
    comm_prefs = ask_communication_style(2, total_categories)
    preferences.update(comm_prefs)
    
    # CATEGORY 3: DOCUMENT PREFERENCES
    doc_prefs = ask_for_document_preferences()
    preferences['document_formatting'] = doc_prefs
    
    # CATEGORY 4: FILE MANAGEMENT
    file_prefs = ask_universal_file_management(4, total_categories)
    preferences['file_management'] = file_prefs
    
    # CATEGORY 5: CODING PREFERENCES
    coding_prefs = ask_coding_preferences(5, total_categories)
    preferences.update(coding_prefs)
    
    print(f"\n{'='*60}")
    print("🎉 **Universal Hints Builder Complete!**")
    print(f"{'='*60}")
    
    print(f"\n📊 **Configuration Summary:** {len(preferences)} categories configured")
    print(f"✅ Platform: {platform_info['system']}")
    print("✅ Custom preferences captured where specified")
    print("✅ Universal file paths configured")
    print("✅ Cross-platform compatibility ensured")
    
    # Generate universal hints file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to user's home directory to avoid permission issues
    output_dir = platform_info['home'] / "goose_hints"
    output_dir.mkdir(exist_ok=True)
    filename = output_dir / f"universal_goose_hints_{timestamp}.txt"
    
    hints_content = f"""# Universal Goose Hints - Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Platform: {platform_info['system']}
# Home Directory: {platform_info['home']}

## Your Personalized Goose Configuration:
"""
    
    for category, prefs in preferences.items():
        hints_content += f"\n### {category.replace('_', ' ').title()}:\n"
        if isinstance(prefs, dict):
            for key, value in prefs.items():
                if isinstance(value, dict) and 'hint' in value:
                    hints_content += f"- {value['hint']}\n"
                else:
                    hints_content += f"- {key}: {value}\n"
        else:
            hints_content += f"- {prefs}\n"
    
    hints_content += f"""
## Universal Features Used:
- Cross-platform compatibility: {platform_info['system']} support
- Universal file paths: Platform-appropriate defaults
- Multiple cloud options: Not limited to single provider
- Custom preferences: Available for all categories
- Flexible organization: Adaptable to your workflow

## Integration Instructions:
1. Copy these hints to your Goose memory system
2. Test with sample tasks to validate preferences
3. Refine any settings based on actual usage
4. Share this configuration template with your team

## File Location:
{filename}
"""
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(hints_content)
        print(f"\n💾 **Universal Hints Saved:** {filename}")
    except Exception as e:
        print(f"\n⚠️  Could not save to {filename}: {e}")
        print("Here's your configuration to copy manually:")
        print("\n" + "="*60)
        print(hints_content)
        print("="*60)
    
    print("\n🚀 **Your Universal Goose Experience is Ready!**")
    print("\n🎯 **Next Steps:**")
    print("1. Save these hints to Goose memory for immediate activation")
    print("2. Test your preferences with a sample task")
    print("3. Adjust any settings based on your experience")
    
    return preferences, hints_content

if __name__ == "__main__":
    try:
        universal_hints_builder()
    except KeyboardInterrupt:
        print("\n\n👋 Universal hints builder cancelled. You can run this anytime!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue so we can improve the universal compatibility!")
