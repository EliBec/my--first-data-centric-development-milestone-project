
$(document).ready(function(){

     /* Initialize Menu burger button */
    $(".button-collapse").sideNav();


    /* Search and Clear buttons will change colors upon clicking any of the search or 'select' fields */
    $("#categorysearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#datesearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#cityorzipsearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#itemsearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#fnamesearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#lnamesearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    /* Clicking on any form field will trigger the change in color for buttons */
    $("#add-form").click(function(){
    $("#add-sale-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clear-all-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });

    $("#update-form").click(function(){
    $("#update-sale-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#cancel-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });


    /* Click the 'Clear' button will reset fields and buttons */
    $("#clearsearch-btn").click(function(){
    $("#search-btn").removeClass("btn btn-info").addClass("btn btn-secondary" );
    $("#clearsearch-btn").removeClass("btn btn-warning").addClass("btn btn-secondary");
    $('#search-form input[type="search"]').val('');
    $('#search-form #datesearch').val('');
    $('#search-form #categorysearch').val('');
    $('#search-form #fnamesearch').val('');
    $('#search-form #lnamesearch').val('');
    });

    /* Click the 'Clear' button will reset fields */
    $("#clear-all-btn").click(function(){   
    $('#add-form input[type="text"]').val('');
    $('#add-form input[type="radio"]').val('');
    $('#add-form #email').val('');
    $('#add-form #telephone').val('');
    $('#add-form #saletime').val('');
    $('#add-form #saledate').val('');
    $('#add-form input[type="radio"]').val('');
    });

    /* Code originally taken from fellow student project https://github.com/LibbyH52/Cookbook-App/blob/master/static/js/script.js and modified to fit my project */
    /* Dynamically add new item for sale to the Add Yard Sale form */
    $(".new-input-btn").on("click", function() {
        $('<input type="text" class="form-control" name="itemlist" placeholder="enter an item(e.g. books)" minlength=3 required/>').insertBefore(".new-input-btn");
    });
    

    /* Code originally taken from fellow student project https://github.com/LibbyH52/Cookbook-App/blob/master/static/js/script.js and modified to fit my project */
    /* remove item from Add Yard Sale form */
    $(".remove-input-btn").on("click", function() {
        $("#additem input:last").remove();
    });


    /* Check the elements on the radio selection type on the form. if there is a value, then make it "checked". Otherwise, assign a "hardcoded" value */
        var garage_sale;
        var garage_sale_elem;
        garage_sale_elem = document.getElementById("garagetypeupd");
        if (garage_sale_elem !== null) {
            garage_sale = garage_sale_elem.value;
        }

        var estate_sale;
        var estate_sale_elem;
        estate_sale_elem = document.getElementById("estatetypeupd");
        if (estate_sale_elem !== null) {
            estate_sale = estate_sale_elem.value;
        }

        var community_sale;
        var community_sale_elem;
        community_sale_elem = document.getElementById("communitytypeupd");
        if (community_sale_elem !== null) {
            community_sale = community_sale_elem.value;
        }

        if (garage_sale == "Garage") {
            document.getElementById("garagetypeupd").checked = true; 
            document.getElementById("estatetypeupd").value = "Estate"; 
            document.getElementById("communitytypeupd").value = "Community"; 
        }

        else if (estate_sale == "Estate") {
                document.getElementById("estatetypeupd").checked = true; 
                document.getElementById("communitytypeupd").value = "Community";
                document.getElementById("garagetypeupd").value = "Garage"; 
        }

        else if (community_sale == "Community") {
                document.getElementById("communitytypeupd").checked = true; 
                document.getElementById("garagetypeupd").value = "Garage"; 
                document.getElementById("estatetypeupd").value = "Estate"; 
        }
});
