from datetime import datetime
from typing import Tuple, List
from profile_scheme import Profile


def experienced_python_dev(profile: Profile) -> Tuple[bool, str]:
    # Check if the person has more than 8 years of total experience
    total_experience_years = 0
    today = datetime.today().date()

    for experience in profile.experiences:
        start_date = datetime.strptime(experience.starts_at, "%Y-%m-%d").date()
        end_date = (
            datetime.strptime(experience.ends_at, "%Y-%m-%d").date()
            if experience.ends_at
            else today
        )
        total_experience_years += (end_date - start_date).days // 365

    if total_experience_years <= 8:
        return False, "Not enough experience"

    # Check if the person worked at a FAANG company in one of the last two work experiences
    faang_companies = {"Facebook", "Apple", "Amazon", "Microsoft", "Google"}

    faang_worked = any(
        experience.company_name in faang_companies
        for experience in profile.experiences[:2]
    )

    if not faang_worked:
        return False, "Never worked at a FAANG company"

    # Check if the position in the last three work experiences is either Backend developer or Software engineer
    positions_last_three = [
        experience.position for experience in profile.experiences[:3]
    ]
    backend_or_software_engineer = any(
        position in {"backend developer", "software engineer"}
        for position in positions_last_three
    )

    if not backend_or_software_engineer:
        return False, "Position in the last three experiences is not Backend developer or Software engineer"

    # Check if worked with Python and C++ in the last position
    last_experience = profile.experiences[0]
    if "Python" not in last_experience.skills_position or "C++" not in last_experience.skills_position:
        return False, "Did not work with Python and C++ in the last position"

    # Check if lives in London
    if profile.location.get("city", "") != "London":
        return False, "Does not live in London"

    return True, ""


def filter_profiles(filter_func, profiles: List[Profile]) -> List[Tuple[str, bool, str]]:
    results = []
    for profile in profiles:
        passed, reason = filter_func(profile)
        result_str = f"{profile.first_name} {profile.surname} – {passed}, {reason}" if not passed \
            else f"{profile.first_name} {profile.surname} – {passed}"
        results.append((result_str, passed, reason))
    return results
