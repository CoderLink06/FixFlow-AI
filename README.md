<p align="center">
  <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/b64dc89c-4620-4059-9fc4-0998673221dc" />
</p>


# ⚡️ FixFlow AI: Zero-Downtime Multi-Agent Orchestrator


** ⚡️Live Demo: [https://fixflow-ai-782015793406.asia-south1.run.app/](https://fixflow-ai-782015793406.asia-south1.run.app/) ⚡️




<p align="center">
  <img width="800" height="300" alt="Screenshot 2026-04-07 203206" src="https://github.com/user-attachments/assets/7c3a6a54-2593-46d6-b8f7-05a83bbaa07f" />

  <img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/15c80a98-8309-49f0-9357-b5b57570578c" />
  

</p>





> **In industrial manufacturing, every minute of downtime costs thousands of dollars. When a machine fails, the process of finding the right manual, checking technician availability, and creating work orders is slow and manual.**



>

>
> 
> <img width="1300" height="800" alt="image" src="https://github.com/user-attachments/assets/c7c2bfa4-e6e1-402a-b6d0-09ebfb450524" />






> **Meet FixFlow AI—a multi-agent orchestrator designed to automate industrial maintenance from alert to resolution.**





<img width="1500" height="900" alt="image" src="https://github.com/user-attachments/assets/a512e534-575e-4391-a2dd-b37299816ec3" />





---

## 🏗️ The GCP Architecture Flex

We built FixFlow AI on a robust, scalable Google Cloud backbone. This isn't just a chatbot; it's an enterprise-grade IoT resolution system.

* **AlloyDB + `pgvector`**: We utilize an AI-ready database to store high-dimensional embeddings of complex machine manuals.
* **Vertex AI (`text-embedding-004`)**: Powers the semantic search, translating technical error codes into actionable fixes.
* **Gemini 1.5 Pro**: Acts as the Primary Coordinator Agent, directing workflow logic.
* **Cloud Pub/Sub**: Ingests live IoT telemetry from the factory floor.
* **Google BigQuery**: Logs all Mean Time To Repair (MTTR) metrics for long-term analytics.
* **Google Workspace API**: Seamlessly integrates with real-world technician calendars.
* **Cloud Run**: Hosts our interactive operations dashboard for zero-cost, scalable deployment.

---

## 🤖 The Multi-Agent Workflow

When an IoT sensor detects an anomaly (e.g., an overheat), our Primary Coordinator Agent immediately initializes and deploys a specialized team of sub-agents:

1.  **The Knowledge Agent:** Performs a semantic vector search on AlloyDB to find the exact fix within the machine manuals.
2.  **The Scheduler Agent:** Communicates with the Google Workspace API to check availability and book a technician.
3.  **The Task Agent:** Dispatches the final work order and required tool list to the technician's device.
4.  **The Analytics Agent:** Exports the resolution data to BigQuery.

---

## 🎬 The "Mic Drop" Moment

This architecture bridges the gap between simulated AI logic and real-world action.

When the workflow completes, the agent doesn't just output text—it prepares a real-world entry in the technician's Google Calendar, pre-filled with the exact parts, tools, and instructions required for the fix.

*(Check out our Live Demo link above to trigger a simulated IoT telemetry alert and watch the sequence play out!)*

---

### 🏆 Hackathon Alignment

FixFlow AI meets all requirements for **Track 1** and **Track 3** by combining Gemini orchestration with AI-ready databases (AlloyDB). We’ve successfully turned hours of industrial downtime into minutes of automated action.



<img width="782" height="461" alt="image" src="https://github.com/user-attachments/assets/63e27347-64d4-4abd-b499-134e9f9f9347" />

