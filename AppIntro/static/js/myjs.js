let init = 1;
$("#add-fitur").on("click", function () {
    ++init;
    if (init <= 6) {
        let tbl = '<span>Fitur ' + init + '</span><div class="form-group">\n' +
            '                    <label>Nama Fitur</label>\n' +
            '                    <input type="text" name="nama-fitur[]" class="form-control" required/>\n' +
            '                </div>' +
            '<div class="form-group">\n' +
            '                    <label>Deskripsi Fitur</label>\n' +
            '                    <textarea class="form-control" name="deskripsi-fitur[]" required></textarea>\n' +
            '                </div>';
        $('#fitur-table > tbody:last-child').append('<tr><td>' + tbl + '</td></tr>');

        //     let table = document.getElementById("");
        //     let row = table.insertRow(1);
        //     let cell1 = row.insertCell(init);

    } else {
        alert("You can't add feature again")
    }
});

$("#submit-form").click(function () {
    $("#form-aplikasi").submit();
});
