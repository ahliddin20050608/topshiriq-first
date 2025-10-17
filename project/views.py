from django.shortcuts import render
from django.http import HttpResponse

def online_dokon(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Noutbuk Doʻkoni</title>

  <style>
    body {
      font-family: "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #f8fafc, #ffffff);
      margin: 0;
      padding: 0;
      color: #0f172a;
    }

    header {
      background: linear-gradient(90deg, #3b82f6, #06b6d4);
      color: #fff;
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }

    header h1 {
      font-size: 22px;
    }

    .search input {
      padding: 8px 12px;
      border-radius: 8px;
      border: none;
      width: 240px;
    }

    .container {
      max-width: 1100px;
      margin: 24px auto;
      padding: 0 20px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 20px;
    }

    .card {
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
      overflow: hidden;
      transition: transform 0.2s;
    }

    .card:hover {
      transform: translateY(-5px);
    }

    .card img {
      width: 100%;
      height: 180px;
      object-fit: cover;
    }

    .card-body {
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .card h3 {
      font-size: 16px;
      margin: 0;
      color: #1e293b;
    }

    .card p {
      font-size: 14px;
      color: #475569;
      flex: 1;
    }

    .price {
      font-weight: bold;
      color: #0ea5e9;
      font-size: 16px;
    }

    .btn {
      background: linear-gradient(90deg, #3b82f6, #06b6d4);
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;
      transition: background 0.3s;
    }

    .btn:hover {
      background: linear-gradient(90deg, #2563eb, #0891b2);
    }

    footer {
      text-align: center;
      padding: 20px;
      color: #64748b;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <header>
    <h1>💻 Noutbuk Doʻkoni</h1>
    <div class="search">
      <input type="text" id="searchBox" placeholder="Noutbuk nomi..." oninput="filterProducts()" />
    </div>
  </header>

  <div class="container">
    <div id="grid" class="grid"></div>
  </div>

  <footer>© <span id="year"></span> Noutbuk Doʻkoni — Barcha huquqlar himoyalangan</footer>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();

    const products = [
      {
        id: 1,
        title: "ASUS TUF Gaming F15",
        description: "Intel i5, RTX 3050, 16GB RAM, 512GB SSD",
        price: 11500000,
        image: "https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Ftweakers.net%2Fext%2Fi%2F2004292096.jpeg&text=ASUS+TUF+Gaming+F15%27&rpt=simage&lr=10336",
      },
      {
        id: 2,
        title: "Apple MacBook Air M2",
        description: "M2 Chip, 8GB RAM, 256GB SSD, 13.6” Retina",
        price: 14200000,
        image: "images/Apple MacBook Air M2.webp",
      },
      {
        id: 3,
        title: "HP Victus 16",
        description: "Ryzen 7, RTX 3060, 16GB RAM, 1TB SSD",
        price: 12900000,
        image: "images/HP Victus 16.webp",
      },
      {
        id: 4,
        title: "Lenovo IdeaPad 5",
        description: "Ryzen 5, 8GB RAM, 512GB SSD, Full HD",
        price: 8700000,
        image: "images/Lenovo IdeaPad 5.webp",
      },
      {
        id: 5,
        title: "Dell XPS 13",
        description: "Intel i7, 16GB RAM, 1TB SSD, QHD ekran",
        price: 15800000,
        image: "images/Dell XPS 13.webp",
      },
    ];

    const grid = document.getElementById("grid");

    function renderProducts(list) {
      grid.innerHTML = "";
      list.forEach((p) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <img src="${p.image}" alt="${p.title}">
          <div class="card-body">
            <h3>${p.title}</h3>
            <p>${p.description}</p>
            <div class="price">${p.price.toLocaleString()} so'm</div>
            <button class="btn" onclick="addToCart('${p.title}')">Savatga qoʻshish</button>
          </div>`;
        grid.appendChild(card);
      });
    }

    function filterProducts() {
      const q = document.getElementById("searchBox").value.toLowerCase();
      const filtered = products.filter((p) =>
        p.title.toLowerCase().includes(q) || p.description.toLowerCase().includes(q)
      );
      renderProducts(filtered);
    }

    function addToCart(title) {
      alert(`${title} savatga qoʻshildi!`);
    }

    renderProducts(products);
  </script>
</body>
</html>
""")