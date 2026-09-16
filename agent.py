import os
import time
from google import genai
from google.genai import types

# =====================================================================
# 1. INITIALIZATION & CREDENTIALS
# =====================================================================
# Your verified fresh API Key from your new Google Cloud Project
API_KEY = "my key"
client = genai.Client(api_key=API_KEY)

# =====================================================================
# 2. EXTENDED NATIVE AGENT TOOLS
# =====================================================================
def read_workspace_code(filename: str) -> str:
    """Reads the raw contents of a specific local file in the workspace."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {filename}: {str(e)}"

def apply_code_patch(filename: str, updated_code: str) -> str:
    """Overwrites or patches a targeted local source code file with corrections."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(updated_code)
        return f"Success: Cleanly patched and updated '{filename}' locally."
    except Exception as e:
        return f"Error writing patch to file: {str(e)}"

def verify_compilation() -> str:
    """Simulates executing a local toolchain compilation check or cross-compiler linter."""
    print("⚡ [TOOL ACTION] Running local static linter and compilation simulator...")
    return "Compilation Status: SUCCESS. 0 errors, 0 warnings."

# Map tools for execution loops
available_tools = {
    "read_workspace_code": read_workspace_code,
    "apply_code_patch": apply_code_patch,
    "verify_compilation": verify_compilation
}

# =====================================================================
# 3. HARDWARE COMPLIANCE POLICY
# =====================================================================
hardware_compliance_rules = """
FIRMWARE POLICY MANUAL:
Rule REQ-001: Clock Gating Verification
When assigning a clock using register 'SYSCTL_RCGCGPIO_R' or 'SYSCTL_RCGCTIMER_R', the software MUST immediately execute a hardware polling loop checking the 'SYSCTL_PRGPIO_R' or 'SYSCTL_PRTIMER_R' bit status respectively. Pins and peripherals cannot have parameters, directions, modes, or interrupts assigned before the peripheral clock is fully stable.
"""

# =====================================================================
# 4. OPTIMIZED CHAT-BASED AGENT EXECUTION LOOP
# =====================================================================
print(" Launching OmniCheck: Embedded Verification Agent...")

agent_prompt = f"""
You are an advanced autonomous embedded firmware auditing agent.
Here is the official hardware design policy manual:
{hardware_compliance_rules}

Your task is to run a multi-step verification and patching loop:
Step 1: Use 'read_workspace_code' to inspect 'main.c' and verify compliance with Rule REQ-001.
Step 2: If any violations are discovered (such as commented-out clock gating stability while loops), modify the code structure cleanly to fix the bug while preserving the rest of the application.
Step 3: Save corrections back to 'main.c' using 'apply_code_patch'.
Step 4: Run 'verify_compilation' to ensure system build success.
Step 5: Output a professional summary of findings and provide a clean Git commit message.
"""

# Open a continuous chat session using 2.5-flash 
chat = client.chats.create(model="gemini-2.5-flash")

# Send initial prompt assignment
response = chat.send_message(
    agent_prompt,
    config=types.GenerateContentConfig(
        tools=[read_workspace_code, apply_code_patch, verify_compilation],
        temperature=0.1 # Technical reasoning constraint
    )
)

# Process step actions dynamically
if response.function_calls:
    print(f"gemini requests using tools...")
    #loop through all the tool requests gemini gave me
    for call in response.function_calls:
        # Add a tiny delay bcz we cant send too many requests at once
        time.sleep(2)
        
        tool_name = call.name
        tool_args = call.args
        print(f" Executing local script tool: {tool_name} with arguments: {tool_args}")
        #if requested tool exist
        if tool_name in available_tools:
            output = available_tools[tool_name](**tool_args)
            
            # Send results straight back through the same chat pipeline
            final_run = chat.send_message(
                f"The tool '{tool_name}' completed. Result: '{output}'. Proceed to final steps and output the confirmation log summary."
            )
            print("\n--- 📊 OmniCheck Pipeline Results ---")
            print(final_run.text)
            break
else:
    print("\n--- Agent Execution Output ---")
    print(response.text)