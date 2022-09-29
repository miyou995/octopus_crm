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
 
// add new item to invoice 
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


  

// let i =1;
// function add(){
//   var table = document.getElementById("table"); 
//   var row = table.insertRow(-1);
//   var th = document.createElement('th');
//   th.setAttribute('scope','row');
//   th.innerHTML= ++i;
//   row.appendChild(th);
//   for (let j=1; j<4;j++){
//     var cell = row.insertCell(j);
//     cell.tabIndex = 1;
//     cell.innerHTML='empty';
//   }
// }



// /*global $, window*/
// $.fn.editableTableWidget = function (options) {
// 	'use strict';
// 	return $(this).each(function () {
// 		var buildDefaultOptions = function () {
// 				var opts = $.extend({}, $.fn.editableTableWidget.defaultOptions);
// 				opts.editor = opts.editor.clone();
// 				return opts;
// 			},
// 			activeOptions = $.extend(buildDefaultOptions(), options),
// 			ARROW_LEFT = 37, ARROW_UP = 38, ARROW_RIGHT = 39, ARROW_DOWN = 40, ENTER = 13, ESC = 27, TAB = 9,
// 			element = $(this),
// 			editor = activeOptions.editor.css('position', 'absolute').hide().appendTo(element.parent()),
// 			active,
// 			showEditor = function (select) {
// 				active = element.find('td:focus');
// 				if (active.length) {
// 					editor.val(active.text())
// 						.removeClass('error')
// 						.show()
// 						.offset(active.offset())
// 						.css(active.css(activeOptions.cloneProperties))
// 						.width(active.width())
// 						.height(active.height())
// 						.focus();
// 					if (select) {
// 						editor.select();
// 					}
// 				}
// 			},
// 			setActiveText = function () {
// 				var text = editor.val(),
// 					evt = $.Event('change'),
// 					originalContent;
// 				if (active.text() === text || editor.hasClass('error')) {
// 					return true;
// 				}
// 				originalContent = active.html();
// 				active.text(text).trigger(evt, text);
// 				if (evt.result === false) {
// 					active.html(originalContent);
// 				}
// 			},
// 			movement = function (element, keycode) {
// 				if (keycode === ARROW_RIGHT) {
// 					return element.next('td');
// 				} else if (keycode === ARROW_LEFT) {
// 					return element.prev('td');
// 				} else if (keycode === ARROW_UP) {
// 					return element.parent().prev().children().eq(element.index());
// 				} else if (keycode === ARROW_DOWN) {
// 					return element.parent().next().children().eq(element.index());
// 				}
// 				return [];
// 			};
// 		editor.blur(function () {
// 			setActiveText();
// 			editor.hide();
// 		}).keydown(function (e) {
// 			if (e.which === ENTER) {
// 				setActiveText();
// 				editor.hide();
// 				active.focus();
// 				e.preventDefault();
// 				e.stopPropagation();
// 			} else if (e.which === ESC) {
// 				editor.val(active.text());
// 				e.preventDefault();
// 				e.stopPropagation();
// 				editor.hide();
// 				active.focus();
// 			} else if (e.which === TAB) {
// 				active.focus();
// 			} else if (this.selectionEnd - this.selectionStart === this.value.length) {
// 				var possibleMove = movement(active, e.which);
// 				if (possibleMove.length > 0) {
// 					possibleMove.focus();
// 					e.preventDefault();
// 					e.stopPropagation();
// 				}
// 			}
// 		})
// 		.on('input paste', function () {
// 			var evt = $.Event('validate');
// 			active.trigger(evt, editor.val());
// 			if (evt.result === false) {
// 				editor.addClass('error');
// 			} else {
// 				editor.removeClass('error');
// 			}
// 		});
// 		element.on('click keypress dblclick', showEditor)
// 		.css('cursor', 'pointer')
// 		.keydown(function (e) {
// 			var prevent = true,
// 				possibleMove = movement($(e.target), e.which);
// 			if (possibleMove.length > 0) {
// 				possibleMove.focus();
// 			} else if (e.which === ENTER) {
// 				showEditor(false);
// 			} else if (e.which === 17 || e.which === 91 || e.which === 93) {
// 				showEditor(true);
// 				prevent = false;
// 			} else {
// 				prevent = false;
// 			}
// 			if (prevent) {
// 				e.stopPropagation();
// 				e.preventDefault();
// 			}
// 		});

// 		element.find('td').prop('tabindex', 1);

// 		$(window).on('resize', function () {
// 			if (editor.is(':visible')) {
// 				editor.offset(active.offset())
// 				.width(active.width())
// 				.height(active.height());
// 			}
// 		});
// 	});

// };
// $.fn.editableTableWidget.defaultOptions = {
// 	cloneProperties: ['padding', 'padding-top', 'padding-bottom', 'padding-left', 'padding-right',
// 					  'text-align', 'font', 'font-size', 'font-family', 'font-weight',
// 					  'border', 'border-top', 'border-bottom', 'border-left', 'border-right'],
// 	editor: $('<input>')
// };
