# omnicheck-firmware-agent

An autonomous agentic workflow for embedded systems engineering powered by the **Google GenAI SDK (`google-genai`)** and **Gemini 2.5 Flash**.

OmniCheck automates hardware compliance verification by analyzing C source files against hardcoded peripheral policy rules (e.g., peripheral clock gating stability checks). When non-compliant code is detected, the agent autonomously reads workspace files, applies patches, and verifies static compilation through native tool calling.

---

## 🌟 Key Features

* **Native Google GenAI Tool Calling:** Leverages Python functions (`read_workspace_code`, `apply_code_patch`, `verify_compilation`) exposed directly to the Gemini agent using `google.genai.types.GenerateContentConfig`.
* **Hardware Policy Enforcement:** Enforces low-level embedded system requirements (such as `SYSCTL_RCGCGPIO_R` and `SYSCTL_PRGPIO_R` polling loop constraints) to prevent hardware configuration faults.
* **Autonomous Self-Healing Loop:** Automatically updates non-compliant code in-place using localized file system patches and validates the build status.
* **Low-Latency Chat Execution:** Utilizes continuous chat sessions (`client.chats.create`) with `gemini-2.5-flash` at low temperature (`0.1`) for deterministic code reasoning.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **AI Model:** Gemini 2.5 Flash (`gemini-2.5-flash`)
* **SDK:** Official Google GenAI SDK (`google-genai`)
* **Execution Tools:** Standard Python File I/O & Tool Execution Loop

---

## 🚀 Getting Started

### Prerequisites

1. Python 3.10 or higher installed.
2. A Google Cloud Gemini API key saved as an environment variable.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/omnicheck-firmware-agent.git](https://github.com/your-username/omnicheck-firmware-agent.git)
   cd omnicheck-firmware-agent
