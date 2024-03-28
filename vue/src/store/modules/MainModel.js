const state = {
    mainModel: [],
    skyBoxImage: [],
    envImage: [],
};
const getters = {
    MAIN_MODEL: (state) => {
        return state.mainModel;
    },
    MAIN_SKY_BOX_IMAGE: (state) => {
        return state.skyBoxImage;
    },
    MAIN_ENV_IMAGE: (state) => {
        return state.envImage;
    },
};
const mutations = {
    SET_MAIN_MODEL: (state, payload) => {
        state.mainModel = payload;
    },
    SET_MAIN_SKY_BOX_IMAGE: (state, payload) => {
        state.skyBoxImage = payload;
    },
    SET_MAIN_ENV_IMAGE: (state, payload) => {
        state.envImage = payload;
    },

};
const actions = {
    GET_MAIN_MODEL: async (context, obj) => {
        await context.commit("SET_MAIN_MODEL", obj?.path);
        await context.commit("SET_MAIN_SKY_BOX_IMAGE", obj?.skyBoxImage)
        await context.commit("SET_MAIN_ENV_IMAGE", obj?.envImage);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
