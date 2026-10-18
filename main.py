"""
Support Ticket Similarity Assistant
Author: Yasir Khan
Description: Matches incoming customer tickets with historical resolutions 
             to assist support agents at Solari Analytics.
"""

import os
import sys

# Here we ensure local imports are working correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from starter_kit.ticket_utils import find_top_matches, load_tickets


def evaluate_incoming_tickets():
    # Below are file paths for historical data and incoming examples
    historical_path = os.path.join("starter_kit", "data", "tickets.json")
    new_tickets_path = os.path.join("starter_kit", "data", "new_tickets_example.json")

    # We are loading datasets
    historical_data = load_tickets(historical_path)
    incoming_data = load_tickets(new_tickets_path)

    print("=" * 65)
    print("SOLARI ANALYTICS - TICKET SIMILARITY ASSISTANT")
    print("=" * 65)
    print(f"Loaded {len(historical_data)} historical tickets.")
    print(f"Evaluating {len(incoming_data)} incoming support requests...\n")

    # Providing a minimum similarity threshold to filter out weak matches (like novel issues)
    similarity_threshold = 0.22

    for index, ticket in enumerate(incoming_data, start=1):
        t_id = ticket.get("ticket_id", f"NT-{index}")
        subject = ticket.get("subject", "")
        desc = ticket.get("description", "")
        combined_text = f"{subject} {desc}"

        print("-" * 65)
        print(f"[{t_id}] Incoming Issue: {subject}")
        print(f"Details: {desc}")
        print("-" * 65)

        # Getting top matching historical tickets
        matches = find_top_matches(combined_text, historical_data, top_n=3)
        valid_matches = [
            (t, score) for t, score in matches if score >= similarity_threshold
        ]

        if not valid_matches:
            print("-> [NOTICE]: No strong historical match found.")
            print("   Action: Likely a novel request (e.g., new integration).")
            print("   Recommendation: Escalate to Tier-2 support and log new resolution.\n")
        else:
            print("-> [MATCH FOUND] Recommended Past Resolutions:")
            for rank, (match_ticket, score) in enumerate(valid_matches, start=1):
                print(f"   {rank}. Match ID: {match_ticket.get('ticket_id')} (Score: {score:.2f})")
                print(f"      Past Subject: {match_ticket.get('subject')}")
                print(f"      Resolution:   {match_ticket.get('resolution_notes')}")
            print()


if __name__ == "__main__":
    evaluate_incoming_tickets()