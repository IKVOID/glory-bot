# -*- coding: utf-8 -*-
import sys, os, time, json, asyncio

if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def main():
    print("=" * 65)
    print("        GUILD GLORY BOT - CONTROL CENTER (SAFE MODE)")
    print("=" * 65)
    print()
    print("  [1] Battle Royale Safe Mode - 1 Squad (Instant ~3s Match & Continuous Glory) [RECOMMENDED]")
    print("  [2] Battle Royale Safe Mode - 1 Squad (Test 1 Match & Auto-Stop)")
    print("  [3] Run All Safe Accounts (7 Accounts, 2 Squads - Continuous Glory)")
    print("  [4] Clash Squad Mode - 1 Squad")
    print("  [5] Single Account Solo Test")
    print()
    print("=" * 65)
    
    choice = input("👉 Option chunein (1, 2, 3, 4, ya 5, default=1): ").strip()
    if not choice:
        choice = "1"

    if choice == "1":
        os.environ["GAME_MODE"] = "BR"
        os.environ["ACCOUNT_LIMIT"] = "4"
        print("\n[*] BATTLE ROYALE: 1 Squad (4 Accounts) Continuous Mode start ho raha hai...")
        print("[*] Target Guild: 3056796518 (Instant Matchmaking ~3s, 100% Safe)")
    elif choice == "2":
        os.environ["GAME_MODE"] = "BR"
        os.environ["ACCOUNT_LIMIT"] = "4"
        os.environ["STOP_AFTER_MATCH"] = "1"
        print("\n[*] BATTLE ROYALE TEST: 1 Match khela jayega aur match khatam hote hi bot auto-stop ho jayega...")
        print("[*] Target Guild: 3056796518")
    elif choice == "3":
        os.environ["GAME_MODE"] = "BR"
        print("\n[*] FULL: Saare 7 Safe accounts (2 Squads) Battle Royale Mode mein start ho rahe hain...")
    elif choice == "4":
        os.environ["GAME_MODE"] = "CS"
        os.environ["ACCOUNT_LIMIT"] = "4"
        print("\n[*] CLASH SQUAD: 1 Squad (4 Accounts) start ho raha hai...")
    elif choice == "5":
        os.environ["TEST_SINGLE_ACCOUNT"] = "1"
        print("\n[*] TEST: 1 Single Account Solo Mode start ho raha hai...")
    else:
        os.environ["GAME_MODE"] = "BR"
        os.environ["ACCOUNT_LIMIT"] = "4"
        print("\n[*] Default: Battle Royale 1 Squad start ho raha hai...")

    print("[*] Web Dashboard: http://127.0.0.1:25086\n")
    time.sleep(1)

    import app
    asyncio.run(app.main())

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Bot band ho gaya.")
