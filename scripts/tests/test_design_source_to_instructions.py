#!/usr/bin/env python3
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from design_source_to_instructions import (  # noqa: E402
    build_instruction,
    instruction_id_for,
    render_markdown,
    slugify,
)


FIXTURE = Path(__file__).resolve().parent / "fixtures" / "sample_source.html"


class DesignSourceToInstructionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.html = FIXTURE.read_text(encoding="utf-8")
        self.instr = build_instruction(
            self.html,
            "https://harborit.example/",
            "SRC-HARBORIT-V1",
        )

    def test_slugify(self) -> None:
        self.assertEqual(slugify("Managed IT Services"), "managed-it-services")

    def test_known_sdts_id(self) -> None:
        self.assertEqual(
            instruction_id_for("https://www.san-diegotechsupport.com/", None),
            "PROD-SDTS-V1",
        )

    def test_extracts_identity_and_it_flag(self) -> None:
        self.assertTrue(self.instr["allowIt"])
        self.assertEqual(self.instr["vertical"], "IT / MSP")
        self.assertEqual(self.instr["nap"]["phone"], "(619) 555-0142")
        self.assertEqual(self.instr["nap"]["email"], "hello@harborit.example")
        self.assertIn("Harbor IT Support", self.instr["businessName"])

    def test_chrome_uses_source_colors(self) -> None:
        colors = set(self.instr["extractedColors"])
        self.assertTrue({"#1b3a4b", "#e8a317", "#0a6aa6"} <= colors)
        self.assertEqual(self.instr["chrome"]["navy"], "#1b3a4b")
        self.assertEqual(self.instr["chrome"]["gold"], "#e8a317")

    def test_hubs_and_forms(self) -> None:
        self.assertGreaterEqual(len(self.instr["hubs"]), 3)
        titles = [h["title"] for h in self.instr["hubs"]]
        self.assertTrue(any("Managed" in t for t in titles))
        roles = [f["role"] for f in self.instr["forms"]]
        self.assertEqual(roles, ["FORM-PRICING", "FORM-SERVICE-REQ"])
        self.assertEqual(len(self.instr["demoHubs"]), 3)

    def test_markdown_round_trip_shape(self) -> None:
        md = render_markdown(self.instr)
        self.assertIn("# SRC-HARBORIT-V1", md)
        self.assertIn("allow IT language", md)
        self.assertIn("Agent brief", md)
        json.dumps(self.instr)  # serializable


if __name__ == "__main__":
    unittest.main()
