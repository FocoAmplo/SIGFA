const state = {

    loading: false,

    conversation: [],

    company: {},

    documents: [],

    knowledge: {},

    diagnosis: {},

    dashboard: {},

    indicators: [],

    charts: [],

    recommendations: [],

    actionPlan: [],

    alerts: [],

    timeline: [],

    logs: [],

    specialist: {}

};

const listeners = [];


function notify() {

    listeners.forEach(listener => listener(state));

}


function subscribe(listener) {

    listeners.push(listener);

    return () => {

        const index = listeners.indexOf(listener);

        if (index >= 0) {

            listeners.splice(index, 1);

        }

    };

}


function getState() {

    return state;

}


function update(payload = {}) {

    state.loading = payload.loading ?? state.loading;

    state.conversation = payload.conversation ?? state.conversation;

    state.company = payload.company ?? state.company;

    state.documents = payload.documents ?? state.documents;

    state.knowledge = payload.knowledge ?? state.knowledge;

    state.diagnosis = payload.diagnosis ?? state.diagnosis;

    state.dashboard = payload.dashboard ?? state.dashboard;

    state.indicators = payload.indicators ?? state.indicators;

    state.charts = payload.charts ?? state.charts;

    state.recommendations = payload.recommendations ?? state.recommendations;

    state.actionPlan = payload.actionPlan ?? state.actionPlan;

    state.alerts = payload.alerts ?? state.alerts;

    state.timeline = payload.timeline ?? state.timeline;

    state.logs = payload.logs ?? state.logs;

    state.specialist = payload.specialist ?? state.specialist;

    notify();

}


function reset() {

    state.loading = false;

    state.conversation = [];

    state.company = {};

    state.documents = [];

    state.knowledge = {};

    state.diagnosis = {};

    state.dashboard = {};

    state.indicators = [];

    state.charts = [];

    state.recommendations = [];

    state.actionPlan = [];

    state.alerts = [];

    state.timeline = [];

    state.logs = [];

    state.specialist = {};

    notify();

}


function setLoading(value) {

    state.loading = value;

    notify();

}


function addMessage(message) {

    state.conversation.push(message);

    notify();

}


export default {

    subscribe,

    getState,

    update,

    reset,

    setLoading,

    addMessage

};