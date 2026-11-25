
def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    prices = {
        "technical": {"low": 20, "medium": 35, "high": 55},
        "billing": {"low": 15, "medium": 25, "high": 40},
        "general": {"low": 10, "medium": 18, "high": 28}
    }

    price = prices[ticket_type][priority_level]
    return price * tickets_resolved


def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_tickets = 1000 + (agent_quarters * 100)
    ticket_capacity = expected_tickets - baseline_tickets

    efficiency = (resolved_tickets - baseline_tickets) / ticket_capacity * 100

    return efficiency


def determine_performance_level(efficiency_percent):
    if efficiency_percent < 50:
        return "Developing Level"
    elif efficiency_percent < 60:
        return "Competent Level"
    elif efficiency_percent < 70:
        return "Proficient Level"
    elif efficiency_percent <= 85:
        return "Advanced Level"
    else:
        return "Expert Level"


def calculate_performance_bonus(value, tickets, level_multiplier):
    base_bonus = value * 0.05 + tickets * 2
    final_bonus = base_bonus * level_multiplier

    return round(final_bonus, 1)


def needs_additional_training(service_weeks, total_tickets, avg_efficiency):
    if service_weeks >= 6 and avg_efficiency < 50:
        return True

    elif total_tickets < 100 and avg_efficiency < 60:
        return True

    elif service_weeks >= 4 and avg_efficiency < 40:
        return True

    else:
        return False


def generate_quality_report(agent_name, ticket_type, tickets,
                            priority_level, agent_quarters,
                            baseline_tickets, resolved_tickets,
                            service_weeks):

    value = calculate_tickets_value(
        ticket_type, tickets, priority_level
    )

    efficiency = calculate_resolution_efficiency(
        agent_quarters, baseline_tickets, resolved_tickets
    )

    performance_level = determine_performance_level(efficiency)

    multipliers = {
        "Developing Level": 0.5,
        "Competent Level": 1.0,
        "Proficient Level": 1.2,
        "Advanced Level": 1.5,
        "Expert Level": 1.8
    }

    multiplier = multipliers[performance_level]

    bonus = calculate_performance_bonus(
        value, tickets, multiplier
    )

    training = needs_additional_training(
        service_weeks, tickets, efficiency
    )

    print(f"Quality Report for: {agent_name}")
    print("----------------------------------------")
    print(f"Ticket Type: {ticket_type}")
    print(f"Tickets Resolved: {tickets}")
    print(f"Priority Level: {priority_level}")
    print(f"Tickets Value: ${value}")

    print("Efficiency Analysis:")
    print(f"  Experience: {agent_quarters} quarters, "
          f"Baseline: {baseline_tickets}, "
          f"Resolved Tickets: {resolved_tickets}")

    print(f"  Efficiency: {efficiency:.1f}%")
    print(f"  Performance Level: {performance_level}")

    print(f"Performance Bonus: ${bonus:.1f}")
    print(f"Service Weeks: {service_weeks}")

    training_result = "Yes" if training else "No"
    print(f"Additional Training Needed: {training_result}")


# MAIN PROGRAM

print("CUSTOMER SERVICE QUALITY MONITOR")
print("========================================")

# Record 1
generate_quality_report(
    "Harper", "technical", 45, "high",
    3, 800, 1150, 3
)

print("\n========================================")

# Record 2
generate_quality_report(
    "Indigo", "billing", 60, "medium",
    5, 900, 1300, 5
)

print("\n========================================")

# Record 3
generate_quality_report(
    "Jesse", "general", 30, "low",
    8, 850, 950, 7
)
