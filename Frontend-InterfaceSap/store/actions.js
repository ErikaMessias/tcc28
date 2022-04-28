export default {
    setProd_seletc(context, payload){
        console.log("payload");
        console.log(payload);
        context.commit("PROD_SELEC", payload);
    },

    setCodigo_seletc(context, payload){
       
        context.commit("COD_SELEC", payload);
    },
};