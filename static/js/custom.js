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
      // var i;
      return {
        items: [{
            id: 0,
            item: 'Service 1',
            price:'1200',
            quantity:'2',
            total:  '1200',
            completed: false
          },
          // {
          //   id: 2,
          //   item: 'Service 2',
          //   price:'100',
          //   quantity:'2',
          //   total: '200',
          //   completed: false
          // }
        ],
        
        addItem() {
        var i=0;

        console.log('THIS WORK');
          //RETURN EMPTY ROW
          this.items.push({
            id: this.items.length ,
            item: 'new Item', 
            price:'0', 
            quantity:'0',
            total:'0',         
            completed: false
          });
          console.log("SIDOU IS TESTING ...");
          // this.newService = '';
          // console.log(document.getElementById("id_items-TOTAL_FORMS"));
          // id_items-0-price
          // document.getElementById(`id_items-${i}-price`).id = `id_items-${i++}-price`;
          // i++;
          // console.log("ferrrr",i);

          const totalForms = document.getElementById("id_items-TOTAL_FORMS") ;
          totalForms.value = this.items.length;
          
          console.log("ferrrrtotalForms",totalForms);
        },
        totalItem(){
          
        },
        deleteItem(serviceId) {
          let position = this.items.findIndex(el => el.id == serviceId);
          this.items.splice(position, 1);
        }

      }
    }

    function manageBillItems() {
        var i=0;
        $('.pt-3-half').each(function(){

        var newID='id_items-'+i+'-price';
        var newName='items-0'+i+'-price';
        $(this).attr('id',newID);
        $(this).attr('name',newName);
        $(this).val(i);
        i++;
  });
    }
