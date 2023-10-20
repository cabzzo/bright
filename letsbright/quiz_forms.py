from django import forms
from .default_profiles import DEFAULT_PROFILES

# Extract unique values from DEFAULT_PROFILES
FOCUS_ASP = list(set(profile.get('goals_dreams', '') for profile in DEFAULT_PROFILES.values() if profile.get('goals_dreams')))
VALUES = list(set(value for profile in DEFAULT_PROFILES.values() for value in profile.get('universal_themes', []) if value))
LEARNING_MEDIUM = list(set(medium for profile in DEFAULT_PROFILES.values() for medium in profile.get('medium', []) if medium))
STYLE = list(set(profile.get('style', '') for profile in DEFAULT_PROFILES.values() if profile.get('style')))
OUTCOMES = list(set(profile.get('outcomes', '') for profile in DEFAULT_PROFILES.values() if profile.get('outcomes')))

# Convert to a format suitable for Django ChoiceField
FOCUS_ASP = [(item, item) for item in FOCUS_ASP]
VALUES = [(item, item) for item in VALUES]
LEARNING_MEDIUM = [(item, item) for item in LEARNING_MEDIUM]
STYLE = [(item, item) for item in STYLE]
OUTCOMES = [(item, item) for item in OUTCOMES]

class OnboardingQuizForm(forms.Form):

    focus_aspiration = forms.ChoiceField(
        choices=FOCUS_ASP,
        widget=forms.RadioSelect,
        label="What is your primary focus or aspiration right now?"
    )

    values = forms.ChoiceField(
        choices=VALUES,
        widget=forms.RadioSelect,
        label="Which of these values resonate with you the most?"
    )

    learning_medium = forms.ChoiceField(
        choices=LEARNING_MEDIUM,
        widget=forms.RadioSelect,
        label="How do you usually learn or get inspired?"
    )

    style = forms.ChoiceField(
        choices=STYLE,
        widget=forms.RadioSelect,
        label="What's your go-to vibe for the spaces you inhabit?"
    )
    
    outcomes = forms.ChoiceField(
        choices=OUTCOMES,
        widget=forms.RadioSelect,
        label="What are you looking to add to your space?"
    )
