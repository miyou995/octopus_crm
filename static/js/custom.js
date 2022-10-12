/**
 *
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 * 
 */
 "use strict";

 $('.alert').show().delay(3000).fadeOut();
        
	function onButtonPress() {
		$('.alert').alert('close');
	  }        
 
// add new item to invoice and proforma
    function items() {
      return {
        items: [{
            id: 1,
            item: 'Service 1',
            price:'1200',
            quantity:'2',
            total:  '1200',
            completed: false
          },
          {
            id: 2,
            item: 'Service 2',
            price:'100',
            quantity:'2',
            total: '200',
            completed: false
          }
        ],
        
        addItem() {
        
          //RETURN EMPTY ROW
          this.items.push({
            id: this.items.length +1,
            item: 'new Item', 
            price:'0', 
            quantity:'0',
            total:'0',         
            completed: false
          });
          // this.newService = '';
        },
        deleteItem(serviceId) {
          let position = this.items.findIndex(el => el.id == serviceId);
          this.items.splice(position, 1);
        }
      }
    }

