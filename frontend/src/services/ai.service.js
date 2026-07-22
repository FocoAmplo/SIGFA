import api from "./api.js";
import intelligenceStore from "../store/intelligence.store.js";

class AIService {

    async send({ prompt, files = [] }) {

        intelligenceStore.setLoading(true);

        intelligenceStore.addMessage({
            role: "user",
            content: prompt
        });

        try {

            const formData = new FormData();

            formData.append("provider", "sigfa");

            formData.append("prompt", prompt);

            files.forEach(file => {

                formData.append("files", file);

            });

            const response = await api.postForm(
                "/ai/chat",
                formData
            );

            this.updateStore(response);

            return response;

        }

        catch (error) {

            intelligenceStore.setLoading(false);

            throw error;

        }

    }

    updateStore(data = {}) {

        intelligenceStore.update({

            loading: false,

            company: data.company || {},

            diagnosis: data.diagnosis || {},

            dashboard: data.dashboard || {},

            indicators: data.indicators || [],

            charts: data.charts || [],

            recommendations: data.recommendations || [],

            actionPlan: data.action_plan || [],

            alerts: data.alerts || []

        });

        if (Array.isArray(data.conversation)) {

            data.conversation.forEach(message => {

                intelligenceStore.addMessage(message);

            });

        }

    }

}

export default new AIService();