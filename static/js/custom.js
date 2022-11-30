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

            // totalItems(){
            //   return this.items.reduce((total, item) => total + item.total, 0)
            // },
            
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
          
          const totalForms = document.getElementById("id_items-TOTAL_FORMS") ;
          totalForms.value = this.items.length;
          
          console.log("ferrrrtotalForms",totalForms);
        },
        
        // total(){
        //   return this.items.reduce((total, item) => total + item.total, 0)
        // },

        deleteItem(serviceId) {
          let position = this.items.findIndex(el => el.id == serviceId);
          this.items.splice(position, 1);
        },        
        totalHorsTaxe(){
          return this.items.reduce((total, item) => total + item.total)

        },


      }

    }

  //   function manageBillItems() {
  //       var i=0;
  //       $('.pt-3-half').each(function(){

  //       var newID='id_items-'+i+'-price';
  //       var newName='items-0'+i+'-price';
  //       $(this).attr('id',newID);
  //       $(this).attr('name',newName);
  //       $(this).val(i);
  //       i++;
  // });
  //   }
  // this.newService = '';
  // console.log(document.getElementById("id_items-TOTAL_FORMS"));
  // id_items-0-price
  // document.getElementById(`id_items-${i}-price`).id = `id_items-${i++}-price`;
  // i++;
  // console.log("ferrrr",i);
  
          // totalPriceItem(){
          //   let price:0, 
          //   quantity:0,
          //   total:0,         
          // },