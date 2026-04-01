from flask import Flask, render_template_string

application = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>KillerNtua — Student Hostels Ghana</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; background: #fdf6f9; color: #2d2d2d; }

    /* NAV */
    nav {
      background: #fff0f5;
      border-bottom: 1.5px solid #f7b8d0;
      padding: 1rem 2rem;
      display: flex; align-items: center; justify-content: space-between;
    }
    .logo { font-size: 1.6rem; font-weight: 700; color: #c0476e; letter-spacing: -0.5px; }
    .logo span { color: #3a9a6e; }
    nav a { color: #c0476e; text-decoration: none; font-size: 0.9rem; margin-left: 1.5rem; }

    /* HERO */
    .hero {
      display: flex; align-items: center; justify-content: space-between;
      padding: 4rem 2rem 2rem; gap: 2rem; max-width: 1100px; margin: 0 auto;
    }
    .hero-text h1 { font-size: 2.6rem; line-height: 1.2; color: #c0476e; max-width: 480px; }
    .hero-text h1 span { color: #3a9a6e; }
    .hero-text p { margin: 1rem 0 1.5rem; color: #666; font-size: 1.05rem; max-width: 420px; }
    .btn {
      background: #c0476e; color: #fff; border: none;
      padding: 0.75rem 2rem; border-radius: 2rem; font-size: 1rem;
      cursor: pointer; text-decoration: none; display: inline-block;
    }
    .btn-outline {
      background: transparent; color: #3a9a6e;
      border: 2px solid #3a9a6e; margin-left: 1rem;
    }

    /* STUDENT MOVE-IN IMAGE (pure CSS illustration) */
    .hero-img {
      flex-shrink: 0; width: 340px; height: 300px;
      background: #fce8f0; border-radius: 1.5rem;
      display: flex; align-items: center; justify-content: center;
      position: relative; overflow: hidden;
      border: 2px solid #f7b8d0;
    }
    .scene { position: relative; width: 100%; height: 100%; }
    /* building */
    .building {
      position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
      width: 200px; height: 200px;
      background: #f2d0e0; border-radius: 8px 8px 0 0;
      border: 2px solid #e8a8c0;
    }
    .door {
      position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
      width: 40px; height: 60px;
      background: #3a9a6e; border-radius: 4px 4px 0 0;
    }
    .window {
      position: absolute; width: 30px; height: 30px;
      background: #a8d8c0; border-radius: 3px; border: 2px solid #3a9a6e;
    }
    .w1 { top: 40px; left: 30px; }
    .w2 { top: 40px; right: 30px; }
    .w3 { top: 100px; left: 30px; }
    .w4 { top: 100px; right: 30px; }
    /* student figure */
    .student {
      position: absolute; bottom: 55px; left: 55px;
    }
    .head {
      width: 28px; height: 28px; border-radius: 50%;
      background: #c8885e; border: 2px solid #a06040;
      margin: 0 auto 2px;
    }
    .body {
      width: 28px; height: 42px;
      background: #c0476e; border-radius: 4px 4px 0 0;
      margin: 0 auto;
    }
    .legs {
      width: 28px; display: flex; gap: 4px; margin: 0 auto;
    }
    .leg {
      flex: 1; height: 28px;
      background: #3a9a6e; border-radius: 0 0 3px 3px;
    }
    /* box (luggage) */
    .box {
      position: absolute; bottom: 55px; left: 86px;
      width: 32px; height: 32px;
      background: #f7b8d0; border: 2px solid #c0476e;
      border-radius: 4px;
    }
    .box::after {
      content: ''; position: absolute;
      top: 50%; left: 0; right: 0; height: 2px;
      background: #c0476e;
    }
    .grass {
      position: absolute; bottom: 0; left: 0; right: 0; height: 55px;
      background: #a8d8a0; border-top: 2px solid #3a9a6e;
    }
    .sun {
      position: absolute; top: 20px; right: 30px;
      width: 40px; height: 40px; border-radius: 50%;
      background: #ffd580;
    }
    .cloud {
      position: absolute; top: 18px; left: 25px;
      background: #fff; border-radius: 20px;
      width: 60px; height: 22px; opacity: 0.85;
    }
    .sign {
      position: absolute; top: 14px; left: 50%; transform: translateX(-50%);
      background: #3a9a6e; color: #fff; font-size: 0.65rem;
      font-weight: 700; padding: 3px 8px; border-radius: 4px; white-space: nowrap;
    }

    /* SEARCH BAR */
    .search-section {
      background: #fff; padding: 2rem; border-radius: 1rem;
      box-shadow: 0 2px 16px rgba(192,71,110,0.08);
      max-width: 700px; margin: 1rem auto 2rem;
    }
    .search-section h2 { color: #c0476e; margin-bottom: 1rem; font-size: 1.2rem; }
    .search-row { display: flex; gap: 0.75rem; flex-wrap: wrap; }
    .search-row select, .search-row input {
      flex: 1; min-width: 150px;
      padding: 0.65rem 1rem; border: 1.5px solid #f7b8d0;
      border-radius: 2rem; font-size: 0.9rem;
      background: #fdf6f9; color: #2d2d2d; outline: none;
    }
    .search-row .btn { white-space: nowrap; }

    /* LISTINGS */
    .listings { max-width: 1100px; margin: 0 auto 3rem; padding: 0 2rem; }
    .listings h2 { color: #3a9a6e; margin-bottom: 1.25rem; font-size: 1.3rem; }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; }
    .card {
      background: #fff; border-radius: 1rem;
      border: 1.5px solid #f7b8d0; padding: 1.25rem;
      transition: transform 0.15s;
    }
    .card:hover { transform: translateY(-3px); }
    .card-tag {
      display: inline-block; font-size: 0.75rem; font-weight: 600;
      padding: 3px 10px; border-radius: 2rem;
      background: #e6f7f0; color: #3a9a6e; margin-bottom: 0.75rem;
    }
    .card h3 { color: #c0476e; font-size: 1rem; margin-bottom: 0.25rem; }
    .card .loc { font-size: 0.82rem; color: #888; margin-bottom: 0.5rem; }
    .card .price { font-size: 1.1rem; font-weight: 700; color: #3a9a6e; margin-bottom: 0.75rem; }
    .card .price span { font-size: 0.8rem; color: #999; font-weight: 400; }
    .card .amenities { font-size: 0.78rem; color: #888; margin-bottom: 1rem; }
    .card .btn { font-size: 0.85rem; padding: 0.5rem 1.25rem; }

    /* FOOTER */
    footer {
      text-align: center; padding: 1.5rem;
      background: #fff0f5; color: #c0476e; font-size: 0.85rem;
      border-top: 1.5px solid #f7b8d0;
    }
    footer span { color: #3a9a6e; }
  </style>
</head>
<body>

<nav>
  <div class="logo">Killer<span>Ntua</span></div>
  <div>
    <a href="#">Home</a>
    <a href="#">Browse</a>
    <a href="#">List a Hostel</a>
    <a href="#">Contact</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-text">
    <h1>Find Your Perfect <span>Student Hostel</span> in Ghana</h1>
    <p>Verified, affordable, and close to campus. GenSa connects Ghanaian students to quality accommodation — fast.</p>
    <a href="#" class="btn">Browse Hostels</a>
    <a href="#" class="btn btn-outline">List My Hostel</a>
  </div>

  <div class="hero-img">
    <div class="scene">
      <div class="cloud"></div>
      <div class="sun"></div>
      <div class="building">
        <div class="sign">GenSa Hostel</div>
        <div class="window w1"></div>
        <div class="window w2"></div>
        <div class="window w3"></div>
        <div class="window w4"></div>
        <div class="door"></div>
      </div>
      <div class="grass"></div>
      <div class="student">
        <div class="head"></div>
        <div class="body"></div>
        <div class="legs"><div class="leg"></div><div class="leg"></div></div>
      </div>
      <div class="box"></div>
    </div>
  </div>
</div>

<div class="search-section">
  <h2>Search Available Hostels</h2>
  <div class="search-row">
    <select>
      <option>Select University</option>
      <option>University of Ghana</option>
      <option>KNUST</option>
      <option>UCC</option>
      <option>UDS</option>
    </select>
    <input type="text" placeholder="Max price (GHS/month)" />
    <select>
      <option>Room type</option>
      <option>Single</option>
      <option>Shared (2)</option>
      <option>Shared (4)</option>
    </select>
    <a href="#" class="btn">Search</a>
  </div>
</div>

<div class="listings">
  <h2>Featured Hostels</h2>
  <div class="cards">

    <div class="card">
      <span class="card-tag">Near UG Legon</span>
      <h3>Akosombo Courts</h3>
      <div class="loc">East Legon, Accra</div>
      <div class="price">GHS 980 <span>/ month</span></div>
      <div class="amenities">WiFi · Security · Water · Kitchen</div>
      <a href="#" class="btn">Book Now</a>
    </div>

    <div class="card">
      <span class="card-tag">Near KNUST</span>
      <h3>Volta View Lodge</h3>
      <div class="loc">Ayigya, Kumasi</div>
      <div class="price">GHS 750 <span>/ month</span></div>
      <div class="amenities">WiFi · Generator · Laundry</div>
      <a href="#" class="btn">Book Now</a>
    </div>

    <div class="card">
      <span class="card-tag">Near UCC</span>
      <h3>Cape Pearl Residence</h3>
      <div class="loc">Pedu, Cape Coast</div>
      <div class="price">GHS 620 <span>/ month</span></div>
      <div class="amenities">Security · Study Room · Water</div>
      <a href="#" class="btn">Book Now</a>
    </div>

  </div>
</div>

<footer>
  &copy; 2025 <span>GenSa</span> — Built for Ghanaian Students. Deployed on <span>AWS Elastic Beanstalk</span>.
</footer>

</body>
</html>
"""

@application.route("/")
def home():
    return render_template_string(HTML)

@application.route("/health")
def health():
    return {"status": "ok", "app": "GenSa", "version": "1.0.0"}

if __name__ == "__main__":
    application.run(debug=True)
