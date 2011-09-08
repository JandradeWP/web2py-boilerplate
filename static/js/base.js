String.prototype.reverse = function () { return this.split('').reverse().join('');};

$(document).ready(function() { 

    //-------------------------------------------------------------- */
    // Jquery UI
    //-------------------------------------------------------------- */
    //
    $("input.date").datepicker({ dateFormat: 'yy-mm-dd', minDate: new Date() });

    //-------------------------------------------------------------- */
    // Inputs
    //--------------------------------------------------------------     
    //
    $('input.integer').live('keyup', function()
            {
                this.value=this.value.reverse().replace(/[^0-9\-]|\-(?=.)/g,'').reverse();
            });
    $('input.double,input.decimal').live('keyup', function()
            {
                this.value=this.value.reverse().replace(/[^0-9\-\.,]|[\-](?=.)|[\.,](?=[0-9]*[\.,])/g,'').reverse();
            });

    //-------------------------------------------------------------- */
    // Tips
    //-------------------------------------------------------------- */

    // Tip for home icon etc.
    $('.tip').poshytip({
        className: 'tip-theme',
        showTimeout: 1,
        alignTo: 'target',
        alignX: 'center',
        alignY: 'bottom',
        offsetX: 0,
        offsetY: 16,
        allowTipHover: false,
        fade: false,
        slide: false
    });

    // Tip that stays
    $('.tip-stay').poshytip({
        className: 'tip-theme',
        showOn:'focus',
        showTimeout: 1,
        alignTo: 'target',
        alignX: 'center',
        alignY: 'bottom',
        offsetX: 0,
        offsetY: 16,
        allowTipHover: false,
        fade: false,
        slide: false
    });

});


