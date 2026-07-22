import AIService from "../services/ai.service.js";
import { showToast } from "./ui.js";

class IntelligenceController {

    initialize() {

        document.addEventListener("click", this.handleClick.bind(this));

    }

    async handleClick(event) {

        if (event.target.id === "ai-upload-button") {

            event.preventDefault();

            document.getElementById("ai-files")?.click();

            return;

        }

        if (event.target.id !== "ai-send") {

            return;

        }

        event.preventDefault();

        await this.send();

    }

    async send() {

        const textarea = document.getElementById("ai-prompt");

        const fileInput = document.getElementById("ai-files");

        const prompt = textarea?.value.trim() || "";

        const files = Array.from(fileInput?.files || []);

        if (!prompt && files.length === 0) {

            showToast(
                "Digite uma pergunta ou envie documentos.",
                "warning"
            );

            return;

        }

        try {

            await AIService.send({

                prompt,

                files

            });

            if (textarea) {

                textarea.value = "";

                textarea.style.height = "auto";

            }

            if (fileInput) {

                fileInput.value = "";

            }

            window.dispatchEvent(

                new CustomEvent(

                    "sigfa:update"

                )

            );

        }

        catch (error) {

            showToast(

                error.message ||

                "Erro ao comunicar com a IA.",

                "error"

            );

        }

    }

}

export default new IntelligenceController();