Vue.component("time_component",{
	template: `
		<div>
			<p>Puede seleccionar un rango de fechas
			para los datos</p>
			<div>
		        <label for="Inicio">Inicio</label>
		        <input
				 type="date"
				v-bind:value="shared.ini_date"
				 v-on:input="updateIniDate($event.target.value)"
				v-bind:max="shared.end_date"
			/>
		    </div>
    		<div>
        		<label for="Fin">Fin</label>
        		<input
				 type="date"
				 v-bind:value="shared.end_date"
                                 v-on:input="updateEndDate($event.target.value)"
				 v-bind:min="shared.ini_date"/>
    		</div>
		</div>
	`,
	mounted(){
		var ini_date = this.$route.query["ini"];
		var end_date = this.$route.query["end"];
		if(ini_date && end_date){
			var d1 = Date.parse(ini_date);
			var d2 = Date.parse(end_date);
			
			if(!d1 || !d2){
				return;
			}
			if(d1>d2){
				return;
			}
		}
		
		if (ini_date){
			this.shared.ini_date = ini_date;
		}
               if (end_date){ 
                        this.shared.end_date = end_date;
                }
		
	},
	data(){
		return {
			shared: store
		}
	},
	methods:{
		updateIniDate(ini_date){
			this.shared.ini_date = ini_date;
			var params = this.shared.getQueryParams();
                        this.$router.replace({query:params});

		},
		updateEndDate(end_date){
			this.shared.end_date = end_date;
			console.log("actualizo end date", end_date)
                        var params = this.shared.getQueryParams();
                        this.$router.replace({query:params});
		}
	}
})
