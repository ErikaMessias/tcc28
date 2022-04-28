export default{
    PROD_SELEC(state, payload){
        state.prod = payload;
    },

    COD_SELEC(state, payload){
        console.log("payload");
        console.log(payload);
        state.cod_sucata = payload;
    },
}