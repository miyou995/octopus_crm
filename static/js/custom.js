/**
 *
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 * 
 */
 "use strict";

 $('.alert').show().delay(20000).fadeOut();
        
	function onButtonPress() {
		$('.alert').alert('close');
	  }        
 
// add new item to invoice and proforma
function items() {
  return {
    items: [{
        id: 0,
        item: ' new item',
        price:0,
        quantity:1,
        total:  0,
        // completed: false
        setQuantity(val) {
          this.quantity = val;
          this.setTotal();
        },
        setPrice(val) {
          this.price = val;
          this.setTotal();
        },
        setTotal(){
          this.total = this.price * this.quantity;
        },
      },
    ],
    
    addItem() {
    console.log('THIS WORK');
      //RETURN EMPTY ROW
      this.items.push({
        id: this.items.length ,
        item: ' new item',
        price:0,
        quantity:1,
        total:  0,
        totalItems: 0,
        // completed: false
        setQuantity(val) {
          this.quantity = val;
          this.setTotal();
        },
        setPrice(val) {
          this.price = val;
          this.setTotal();
        },
        setTotal(){
          this.total = this.price * this.quantity;
        },         
        // completed: false
      });
      console.log(this.addItem)
      const totalForms = document.getElementById("id_items-TOTAL_FORMS") ;
      totalForms.value = this.items.length;
      
      console.log("ferrrrtotalForms",totalForms);
    },
    
    totalHorsTaxe(){

      console.log("THIS OIS TJHE TOTAL:= ",this.items.reduce((total, item) => total + item.total, 0))
      return this.items.reduce((total, item) => total + item.total, 0)+" DA"

    },

    deleteItem(serviceId) {
      let position = this.items.findIndex(el => el.id == serviceId);
      this.items.splice(position, 1);
    },     
  }
}
