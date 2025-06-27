#!/usr/bin/env python3
"""
Password Security Tool
- Analyzes password strength using zxcvbn
- Generates custom wordlists for penetration testing
"""

import argparse
import logging
import os
from datetime import datetime
from zxcvbn import zxcvbn

# ======================
# LOGGING CONFIGURATION
# ======================
log_file = os.path.abspath('password_tool.log')  # Full path for debugging

# Clear any existing log handlers
logging.getLogger().handlers = []

# Configure logging
logging.basicConfig(
    filename=log_file,
    filemode='a',  # Append mode
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True  # Override any existing configs
)

# ======================
# CORE FUNCTIONS
# ======================

def analyze_password(password):
    """Analyze password strength using zxcvbn"""
    try:
        result = zxcvbn(password)
        logging.info(f"Analyzed: '{password}' | Score: {result['score']}/4")
        return {
            'password': password,
            'score': result['score'],
            'feedback': result['feedback']['warning'] or "No major weaknesses",
            'crack_time': result['crack_times_display']['online_no_throttling_10_per_second']
        }
    except Exception as e:
        logging.error(f"Password analysis failed: {str(e)}")
        raise

def generate_wordlist(keywords, years):
    """Generate custom wordlist for brute-force testing"""
    try:
        wordlist = []
        
        # Basic combinations
        for word in keywords:
            wordlist.append(word)
            for year in years:
                wordlist.append(f"{word}{year}")
                wordlist.append(f"{word.upper()}{year}")
        
        # Leet-speak substitutions
        leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
        for word in wordlist.copy():
            for char, replacement in leet_map.items():
                if char in word.lower():
                    wordlist.append(word.lower().replace(char, replacement))
        
        # Save to timestamped file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"wordlist_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("\n".join(wordlist))
        
        logging.info(f"Generated wordlist with {len(wordlist)} entries: {filename}")
        return filename
        
    except Exception as e:
        logging.error(f"Wordlist generation failed: {str(e)}")
        raise

# ======================
# COMMAND LINE INTERFACE
# ======================

def main():
    parser = argparse.ArgumentParser(
        description="Password Security Tool - Analyze strength or generate attack wordlists",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Password analysis mode
    parser.add_argument(
        '-p', '--password',
        help="Password to analyze (e.g., 'P@ssw0rd123!')"
    )
    
    # Wordlist generation mode
    parser.add_argument(
        '-g', '--generate',
        action='store_true',
        help="Enable wordlist generation mode"
    )
    parser.add_argument(
        '-k', '--keywords',
        help="Comma-separated keywords (e.g., 'john,dog,admin')"
    )
    parser.add_argument(
        '-y', '--years',
        help="Comma-separated years (e.g., '2020,2025')"
    )
    
    args = parser.parse_args()
    
    # Initialize logging
    logging.info("\n" + "="*50)
    logging.info(f"NEW SESSION STARTED AT {datetime.now()}")
    
    try:
        # Password analysis
        if args.password:
            result = analyze_password(args.password)
            print("\n[PASSWORD ANALYSIS]")
            print(f"Password: {result['password']}")
            print(f"Strength: {result['score']}/4")
            print(f"Feedback: {result['feedback']}")
            print(f"Crack Time: {result['crack_time']}")
        
        # Wordlist generation
        if args.generate:
            if not args.keywords or not args.years:
                raise ValueError("Both --keywords and --years are required for wordlist generation")
                
            keywords = [k.strip() for k in args.keywords.split(',')]
            years = [y.strip() for y in args.years.split(',')]
            
            filename = generate_wordlist(keywords, years)
            print(f"\n[WORDLIST GENERATED] Saved to: {filename}")
            print(f"Use with tools like Hashcat: `hashcat -a 0 -m 100 hashes.txt {filename}`")
    
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")
        print(f"\n[ERROR] {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    import sys
    print(f"Logging to: {log_file}")  # Show user where logs are saved
    main()
