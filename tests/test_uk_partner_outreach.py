"""The UK adult-learner partner outreach setup: config and skill wiring."""

from pathlib import Path

from harvey.brain import Brain
from harvey.config import load_config

ROOT = Path(__file__).resolve().parent.parent


def test_shipped_config_targets_uk_partners():
    config = load_config(str(ROOT / "harvey.yaml"))
    assert config.persona.company == "Your Company"   # refuses to run until filled in
    assert config.usage.quiet_hours.timezone == "Europe/London"
    assert set(config.icp.geography) <= set(config.icp.geo_coordinates)


def test_course_rules_reach_every_writing_agent():
    brain = Brain.__new__(Brain)
    for agent in ("scout", "writer", "handler", "sender"):
        assert "UK Adult Learner Courses" in brain.load_skills_for_agent(agent), agent
