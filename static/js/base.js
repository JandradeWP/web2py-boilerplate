String.prototype.reverse = function () { return this.split('').reverse().join('');};

$(document).ready(function() { 

  //-------------------------------------------------------------- */
  // Alerts
  //-------------------------------------------------------------- */
  //
  $('div.alert-message > a.close').click(function () {
    $(this).parent().fadeOut();
    return false;
  });

  //-------------------------------------------------------------- */
  // Tabs
  //-------------------------------------------------------------- */
  //
  var tab_content = $('div.tabs > div');
  tab_content.hide().filter(':first').show();

  $('div.tabs ul.tabs a').click(function () {
    tab_content.hide();
    tab_content.filter(this.hash).show();
    $('div.tabs ul.tabs li').removeClass('active');
    $(this).parent().addClass('active');
    return false;
  }).filter(':first').click();

  //-------------------------------------------------------------- */
  // Pills
  //-------------------------------------------------------------- */
  //
  var pill_content = $('div.pills > div');
  pill_content.hide().filter(':first').show();

  $('div.pills ul.pills a').click(function () {
    pill_content.hide();
    pill_content.filter(this.hash).show();
    $('div.pills ul.pills li').removeClass('active');
    $(this).parent().addClass('active');
    return false;
  }).filter(':first').click();

  //-------------------------------------------------------------- */
  // Dropdown
  //-------------------------------------------------------------- */
  //
  $("body").bind("click", function (e) {
    $('.dropdown-toggle, .web2py-menu-expand > a, .menu').parent("li").removeClass("open");
  });
  $(".dropdown-toggle, .web2py-menu-expand > a, .menu").click(function (e) {
    var $li = $(this).parent("li").toggleClass('open');
    return false;
  });

  //-------------------------------------------------------------- */
  // Jquery UI
  //-------------------------------------------------------------- */
  //
  //$("input.date").datepicker({ dateFormat: 'yy-mm-dd', minDate: new Date() });
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
  // Tips$("input.date").datepicker({ dateFormat: 'yy-mm-dd', minDate: new Date() });

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


