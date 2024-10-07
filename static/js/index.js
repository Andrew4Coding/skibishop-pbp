async function getProducts() { 
    const res = await fetch(`${window.location.href}json`).then(response => response.json()).catch(error => console.error(error));
    return res;
}

async function refreshProducts() {
    console.log("Refreshing products...");
    
    document.getElementById("product-container").innerHTML = "";

    const products = await getProducts();


    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        htmlString = "<p>No products found</p>";
    }
    else {
        classNameString="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10";
        products.forEach(product => {
            htmlString += `
                <div
                    class="rounded-3xl w-full md:w-[260px] border-[1px] border-black/10 shadow-xl p-5 text-black hover:shadow-xl cursor-pointer transition-all duration-300 flex flex-col gap-5"
                >
                    <div class="w-full h-[200px] bg-[#F6F6F6] rounded-xl p-8 relative">
                        <img
                            src="https://pngimg.com/d/macbook_PNG61.png"
                            class="w-full object-contain h-full rounded-xl"
                        />
                    </div>
                        <div
                            class="flex flex-col "
                        >
                            <h3 class="m-0 font-medium text-sm">${ product.fields.name }</h3>
                            <h1 class="m-0 text-xl font-bold">Rp${product.fields.price}</h1>
                            <h3 class="m-0 font-medium text-sm text-[#737373]">by AndrewStore</h3>
                            <h3 class="font-medium text-sm">4k Terjual</h3>
                            <div class="flex my-2 gap-2" >
                                <a href='edit/${product.pk}' class="w-full">
                                    <button class="bg-[#7C00FE] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Edit</button>
                                </a>
                                <a href='delete/${product.pk}' class="w-full">
                                    <button class="bg-[#D91656] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Delete</button>
                                </a>
                            </div>
                        </div>
                </div>
            `;
        });
    }

    document.getElementById("product-container").className = classNameString;
    document.getElementById("product-container").innerHTML = htmlString;
}

function addProduct() { 
    console.log(new FormData(document.querySelector('#productEntryForm')));
    
    fetch(`${window.location.href}create-product-form-ajax`, {
        method: "POST",
        body: new FormData(document.querySelector('#productEntryForm')),
    })
        .then(response => {
            console.log(response);
            refreshProducts();
        }).catch(error => console.error(error));
    
    document.getElementById("productEntryForm").reset();
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
}

document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProduct();
})

const modal = document.getElementById('crudModal');
const modalContent = document.getElementById('crudModalContent');

function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden');
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);

document.getElementById("submitProductEntry").onclick = addProduct;

refreshProducts();