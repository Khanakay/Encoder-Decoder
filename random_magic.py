import random

phrases = {
    0: [
        "Wake up",
        "Brush teeth",
        "Take a shower",
        "Get dressed",
        "Make breakfast",
        "Eat breakfast",
        "Check emails",
        "Respond to emails",
        "Attend meetings",
        "Complete work assignments",
        "Take a break",
        "Go for a walk",
        "Make a phone call",
        "Attend a class",
        "Do homework",
        "Read a book",
        "Do laundry",
        "Clean the house",
        "Wash dishes",
        "Take out the trash",
        "Go grocery shopping",
        "Cook dinner",
        "Eat dinner",
        "Watch TV",
        "Exercise",
        "Meditate",
        "Plan for the next day",
        "Go to bed",
        "Feed the pets",
        "Water the plants",
        "Check social media",
        "Write in a journal",
        "Pay bills",
        "Attend an event",
        "Visit a friend",
        "Call family",
        "Practice a hobby",
        "Run errands",
        "Drive to work",
        "Commute home",
        "Prepare a presentation",
        "Attend a webinar",
        "Organize workspace",
        "Check calendar",
        "Make a to-do list",
        "Review goals",
        "Set reminders",
        "Charge devices",
        "Clean computer files",
        "Backup data",
        "Update software",
        "Install updates",
        "Clean car",
        "Refuel car",
        "Review budget",
        "Shop online",
        "Check news",
        "Follow up on tasks",
        "Prepare snacks",
        "Take medication",
        "Plan meals",
        "Check weather",
        "Organize documents",
        "Attend a workshop",
        "Write reports",
        "File paperwork",
        "Sort mail",
        "Groom pets",
        "Mow the lawn",
        "Schedule appointments",
        "Call a repair service",
        "Update resume",
        "Apply for jobs",
        "Review applications",
        "Check finances",
        "Review subscriptions",
        "Cancel unused services",
        "Repair household items",
        "Plan travel",
        "Pack for a trip",
        "Organize photos",
        "Declutter home",
        "Donate unused items",
        "Volunteer",
        "Attend a social event",
        "Buy gifts",
        "Wrap gifts",
        "Send thank you notes",
        "Review insurance policies",
        "Check credit score",
        "Research investments",
        "Meet with a financial advisor",
        "Plan a party",
        "Host a gathering",
        "Prepare for a meeting",
        "Update website",
        "Post on blog",
        "Review analytics"
    ]
}

def get_random_phrase():
    return random.choice(phrases[0])

random_phrase = get_random_phrase()

