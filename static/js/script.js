/* Search and Clear buttons will change colors upon clicking any of the search or 'select' fields */
$(document).ready(function(){
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

    $("#namesearch").click(function(){
    $("#search-btn").removeClass("btn btn-secondary").addClass("btn btn-info" );
    $("#clearsearch-btn").removeClass("btn btn-secondary").addClass("btn btn-warning" );
    });
    

    /* Click the 'Clear button will reset fields and buttons */
    $("#clearsearch-btn").click(function(){
    $("#search-btn").removeClass("btn btn-info").addClass("btn btn-secondary" );
    $("#clearsearch-btn").removeClass("btn btn-warning").addClass("btn btn-secondary");
    $('#search-form input[type="search"]').val('');
    $('#search-form #date-search').val('');
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


    var garage_sale = document.getElementById("garagetypeupd").value;
    var state_sale = document.getElementById("statetypeupd").value;
    var community_sale = document.getElementById("communitytypeupd").value;

    if (garage_sale == "garage") {
        document.getElementById("garagetypeupd").checked = true; 
        document.getElementById("statetypeupd").value = "state"; 
        document.getElementById("communitytypeupd").value = "community"; 
    }

    else if (state_sale == "state") {
            document.getElementById("statetypeupd").checked = true; 
            document.getElementById("communitytypeupd").value = "community";
            document.getElementById("garagetypeupd").value = "garage"; 
    }

    else if (community_sale == "community") {
             document.getElementById("communitytypeupd").checked = true; 
             document.getElementById("garagetypeupd").value = "garage"; 
             document.getElementById("statetypeupd").value = "state"; 
    }

});
