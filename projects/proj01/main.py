"""
=============================================================================
Course: CS-31 Python Programming
Project: Referee Assignr - Simulated Sales Conversation & Game Assignment
# Student: Carlos Farias
# Date 10/25/2026
=============================================================================
### Project Context & Objective
A regional soccer game assignor managing 4 major youth & amateur leagues across 7 
Pennsylvania counties (Berks, Dauphin, Bucks/Ducks, Lancaster, Montgomery, Chester, and Lebanon) 
requires a prototype program that simulates an interactive sales and registration conversation 
with a licensed USSF soccer referee.

This Jupyter Notebook satisfies all 15 operational steps detailed in `V11_RefereeAssignr.pdf` and incorporates data from the tournament management tables:
- **`Leagues.txt`**: Directory of participating leagues and team breakdowns by age bracket.
- **`Facilities.txt`**: Venues, complexes, addresses, and field counts across PA counties.
- **`Categories.txt`**: Age categories, division duration, halftime intervals, and total time slots.
- **`Teams.txt`**: Registered youth squads, divisions, genders, and league affiliations.
- **`Main11.txt`**: Mastner match schedule comprising 236 fixtures across 5 tournament weekends.
=============================================================================
"""

def main():
    # -----------------------------------------------------------------------
    # STEP 1: GREETING & PROGRAM PRESENTATION
    # -----------------------------------------------------------------------
    print("=" * 65)
    print("       WELCOME TO THE REFEREE ASSIGNR VIRTUAL ASSISTANT")
    print("=" * 65)
    print("AssignrBot: Hello and welcome! I am AssignrBot, your dedicated")
    print("            soccer officiating concierge for the 2026 season.")
    print("AssignrBot: We manage premier match assignments across 4 major leagues:")
    print("            - PA Classics (LG01): 44 Teams across Boys & Girls divisions")
    print("            - MLS (LG02): 38 Elite Teams across U13-U19 divisions")
    print("            - Europa Boys (LG03): 23 High-Powered Boys Teams")
    print("            - NAL (LG05): 38 Competitive Teams across age brackets")
    print()

    # -----------------------------------------------------------------------
    # STEP 2: INQUIRY ABOUT QUANTITY & QUALITY OF GAMES
    # -----------------------------------------------------------------------
    learn_more = input("AssignrBot: Would you like more information about the quantity\n"
                       "            and quality of games available this season? (y/n): ")
    print()

    # -----------------------------------------------------------------------
    # STEPS 3 & 4: OVERVIEW OR POLITE FAREWELL
    # -----------------------------------------------------------------------
    if learn_more.strip().lower() != "y":
        print("AssignrBot: No problem at all! Thank you for considering our assignment")
        print("            network. Best of luck with your upcoming season! Goodbye.")
        print("=" * 65)
        input("\n[Press Enter to return to IDLE...]")
        return

    print("AssignrBot: Fantastic! Here is a high-level briefing of our network:")
    print("            • Participating Leagues: PA Classics, MLS, Europa Boys, NAL")
    print("            • Match Counties: Berks, Dauphin, Ducks, Lancaster,")
    print("                              Montgomery, and Lebanon")
    print("            • Age Brackets: U13, U14, U15, U16, U17, and U19 (Boys & Girls)")
    print("            • Top Facilities: The Proving Grounds, Spooky Nook LANCO,")
    print("                              BIG Vision Complex, Kelly Field, and more!")
    print()

    # -----------------------------------------------------------------------
    # STEP 5: CREATIVE & DETAILED PROGRAM DESCRIPTION
    # -----------------------------------------------------------------------
    print("-" * 65)
    print("AssignrBot: Picture this: crisp weekend mornings on state-of-the-art")
    print("            turf fields, high-stakes competition with elite academies,")
    print("            and seamless schedules tailored around your travel preferences.")
    print("            Over 230 matches are scheduled across 5 action-packed weekends")
    print("            running from August 8 through September 20, 2026.")
    print("            Whether you prefer center refereeing under the stadium lights")
    print("            or running lines on high-tempo U19 showcases, our assignment")
    print("            system ensures you get the match quality you deserve!")
    print("-" * 65)
    print()

    # -----------------------------------------------------------------------
    # STEP 6: PURCHASE / REGISTRATION INTENT
    # -----------------------------------------------------------------------
    join_assignr = input("AssignrBot: Does this sound like an assignment service you would\n"
                         "            like to register with today? (y/n): ")
    print()

    if join_assignr.strip().lower() != "y":
        print("AssignrBot: We completely understand. Feel free to reach back out when")
        print("            you are ready to pick up games. Have a wonderful day!")
        print("=" * 65)
        input("\n[Press Enter to return to IDLE...]")
        return

    # -----------------------------------------------------------------------
    # STEP 7: CLOSE THE SALE - REFEREE INTAKE & VALIDATION
    # -----------------------------------------------------------------------
    print("AssignrBot: Outstanding! Let's get your referee profile established.")
    print()

    # 7a. Name variables
    first_name = input("AssignrBot: First, what is your first name? ").strip()
    last_name = input("AssignrBot: And your last name? ").strip()

    # 7b. USSF ID (16-digit format)
    ussf_id = input("AssignrBot: What is your 16-digit USSF ID (e.g., 0000-0000-0000-0000)? ").strip()

    # 7c. Email
    email = input("AssignrBot: What is your preferred email address? ").strip()

    # 7d. Address breakdown & Phone
    print("AssignrBot: To match you with facilities near your residence, please enter")
    print("            your full home address details:")
    street_address = input("            • Street Address: ").strip()
    apartment_unit = input("            • Apartment/Unit (or 'N/A'): ").strip()
    city = input("            • City: ").strip()
    county = input("            • County (e.g., Lancaster, Berks): ").strip()
    zip_code = input("            • ZIP Code: ").strip()
    state = input("            • State (e.g., PA): ").strip()
    phone_number = input("AssignrBot: Finally, your phone number (format: 01-999-456-4589): ").strip()
    print()

    # 7e. Legal status check (Boolean)
    work_auth_input = input("AssignrBot: Are you a legal US resident authorized to work in the US? (yes/no): ").strip().lower()
    is_work_authorized = (work_auth_input == "yes" or work_auth_input == "y")

    if not is_work_authorized:
        print()
        print("AssignrBot: Notice: Selecting 'No' disqualifies you from working")
        print("            USOfficials / USSF sanctioned events due to legal compliance.")
        print("            We are unable to proceed with registration at this time. Goodbye.")
        print("=" * 65)
        input("\n[Press Enter to return to IDLE...]")
        return

    # 7f. Maximum referee experience level
    print()
    print("AssignrBot: What is your maximum referee experience level in the last 12 months?")
    print("            [1] Youth (U5–U19)")
    print("            [2] Youth Elite (MLS-N, GA, ECNL)")
    print("            [3] College (NCAA, NJCAA, NAIA)")
    print("            [4] American Adult Leagues (Local, State, and Regional)")
    print("            [5] Adult Pro-Am Leagues (UPSL, USL2, NPSL, WPSL)")
    print("            [6] Professional (USL1/C+, NWSL, MLS)")
    exp_choice = input("AssignrBot: Enter choice (1-6): ").strip()

    if exp_choice == "1":
        experience_level = "Youth (U5–U19)"
    elif exp_choice == "2":
        experience_level = "Youth Elite (MLS-N, GA, ECNL)"
    elif exp_choice == "3":
        experience_level = "College (NCAA, NJCAA, NAIA)"
    elif exp_choice == "4":
        experience_level = "American Adult Leagues"
    elif exp_choice == "5":
        experience_level = "Adult Pro-Am Leagues"
    else:
        experience_level = "Professional (USL1/C+, NWSL, MLS)"

    # 7g. Full season availability (Boolean)
    season_avail_input = input("AssignrBot: Are you available for the entire 5-weekend tournament season? (yes/no): ").strip().lower()
    is_available_entire_season = (season_avail_input == "yes" or season_avail_input == "y")
    print()

    # -----------------------------------------------------------------------
    # STEP 8: EXPLANATION OF ASSIGNMENT RULES
    # -----------------------------------------------------------------------
    cr_role = "Center Referee"
    ar1_role = "Assistant Referee 1"
    ar2_role = "Assistant Referee 2"

    print("=" * 65)
    print("             OFFICIAL REFEREE ASSIGNMENT RULES")
    print("=" * 65)
    print(f"1. Officiating Trio: Every match assigns three officials:")
    print(f"   - {cr_role} (CR), {ar1_role} (AR1), and {ar2_role} (AR2).")
    print(f"2. Strict Rotation Protocol:")
    print(f"   - When assigned as {cr_role}, your next consecutive game is scheduled as {ar2_role}.")
    print(f"   - If you served as {ar2_role}, your subsequent game is scheduled as {ar1_role}.")
    print("3. Daily Load & Recovery:")
    print("   - Maximum limit of 6 assigned games per day.")
    print("   - Mandatory 1-game break between any set of 3 consecutive matches.")
    print("4. Check-In & Reporting:")
    print("   - Must arrive 30 minutes before your opening match to check in at table.")
    print("   - Only the Center Referee (CR) submits final match scores.")
    print("   - Only the Center Referee (CR) files Yellow Card (YC) & Red Card (RC) reports,")
    print("     including team names and player jersey numbers.")
    print("5. Season Calendar:")
    print("   - The tournament spans 5 weekends. Women's divisions kick off one week")
    print("     after the Men's divisions.")
    print("=" * 65)
    print()

    # -----------------------------------------------------------------------
    # STEPS 9 & 10: AVAILABLE MATCHES & RATES OVERVIEW
    # -----------------------------------------------------------------------
    print("AssignrBot: Here are the current assignment service packages and referee")
    print("            rates based on age categories:")
    print("-" * 65)
    print(f"{'Category':<10} {'Divisions':<22} {'Match Pay (CR / AR)':<20} {'Service Fee'}")
    print("-" * 65)
    print(f"{'U13 - U14':<10} {'Boys & Girls (35m H)':<22} {'$60.00 / $50.00':<20} {'$12.50 / game'}")
    print(f"{'U15':<10} {'Boys & Girls (40m H)':<22} {'$65 - $70 / $55':<20} {'$15.00 / game'}")
    print(f"{'U16 - U17':<10} {'Boys & Girls (45m H)':<22} {'$105 - $110 / $65':<20} {'$18.00 / game'}")
    print(f"{'U19':<10} {'Showcase (45m H)':<22} {'$130 - $150 / $74':<20} {'$20.00 / game'}")
    print("-" * 65)
    print("AssignrBot: Note: A flat assignor administrative service fee of $15.00 per game")
    print("            covers automated scheduling, assignor insurance, and priority slotting.")
    print()

    # -----------------------------------------------------------------------
    # STEPS 11, 12, & 13: GAME SELECTION & COST CALCULATIONS
    # -----------------------------------------------------------------------
    service_rate_per_game = 15.00
    tax_rate = 0.10  # 10% administrative processing fee

    while True:
        num_games_input = input("AssignrBot: How many game assignments would you like to purchase\n"
                                "            for scheduling this season? (Max 6 per day): ").strip()
        try:
            num_games = int(num_games_input)
            if num_games > 0:
                break
            else:
                print("AssignrBot: Please enter a positive number of games.")
        except ValueError:
            print("AssignrBot: Please enter a valid whole number.")

    # Basic arithmetic calculations
    subtotal = num_games * service_rate_per_game
    admin_tax = subtotal * tax_rate
    total_due = subtotal + admin_tax

    print()
    print("AssignrBot: Processing your assignment roster...")
    print()

    # -----------------------------------------------------------------------
    # STEP 14: FORMATTED RECEIPT OUTPUT (MODELED AFTER PROJECT IMAGES)
    # -----------------------------------------------------------------------
    print("=" * 65)
    print("             REFEREE ASSIGNMENT REGISTRATION RECEIPT")
    print("=" * 65)
    print(f"Referee Name  : {first_name} {last_name}")
    print(f"USSF ID       : {ussf_id}")
    print(f"Email         : {email}")
    print(f"Phone         : {phone_number}")
    print(f"Home Address  : {street_address}, {apartment_unit}, {city}, {county}, {state} {zip_code}")
    print(f"Experience    : {experience_level}")
    print(f"Full Season?  : {'Yes' if is_available_entire_season else 'Partial'}")
    print("-" * 65)
    print(f"Quantity      : {num_games} game assignment(s)")
    print(f"Service Rate  : ${service_rate_per_game:.2f} per game")
    print("-" * 65)
    print(f"Subtotal      : ${subtotal:.2f}")
    print(f"Admin Tax(10%): ${admin_tax:.2f}")
    print("=" * 65)
    print(f"Total Due     : ${total_due:.2f}")
    print("=" * 65)
    print()

    # -----------------------------------------------------------------------
    # STEP 15: FAREWELL & CONFIRMATION MESSAGE
    # -----------------------------------------------------------------------
    print(f"AssignrBot: Thank you for registering, {first_name}!")
    print("AssignrBot: A confirmation receipt and assignment link have been emailed to")
    print(f"            {email}.")
    print("AssignrBot: Your localized match assignments near ZIP code " + zip_code + " will be")
    print("            published on your portal within 3 business days.")
    print("AssignrBot: Have a fantastic officiating season, and see you on the pitch!")
    print("=" * 65)

    input("\n[Program completed. Press Enter to exit...]")

if __name__ == "__main__":
    main()