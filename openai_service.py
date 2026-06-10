import time

def generate_social_posts(business_description, tone, business_goal):
    """
    Wannan ingantaccen gurbin gwaji ne (Smart Mock Function) na Brightins.
    Yana duba kalmomin da aka shigar don samar da hashtags da rubutu masu dacewa,
    har da tallan Hausa na musamman don jarrabawa (Demo).
    """
    # Jinkirin daƙiƙa 1.5 don kwaikwayon tunanin AI
    time.sleep(1.5)
    
    desc = business_description.strip() if business_description.strip() else "our premium products and services"
    desc_lower = desc.lower()
    
    # 1. DEFAULTS (Tsarin asali idan ba a gane kalmar ba)
    hashtags = ["#BusinessGrowth", "#GlobalBrand", "#QualityService", "#Innovation"]
    
    facebook_post = (
        f"Are you looking for the best way to elevate your lifestyle and experience true quality? "
        f"Look no further, we’ve got exactly what you need!\n\n"
        f"Introducing: {desc}.\n\n"
        f"We take pride in delivering excellence tailored specifically to your satisfaction. "
        f"Whether you are buying for personal use or looking to partner with us on a larger scale, "
        f"we guarantee premium standards every single time.\n\n"
        f"📥 Send us a DM or drop a comment below to get started today! 🚀"
    )
    
    instagram_caption = (
        f"Quality is not an act, it is a habit. ✨\n\n"
        f"Discover the ultimate difference with: {desc}.\n\n"
        f"Crafted with precision, delivered with passion, and designed to meet global standards. "
        f"Don't settle for less when you can have the premium experience you truly deserve.\n\n"
        f"🔗 Click the link in our bio to shop now or chat with our customer support team! 💎"
    )
    
    twitter_post = (
        f"Looking to scale up? It all starts with choosing the right quality. \n\n"
        f"Check out: {desc} 🌍\n\n"
        f"Engineered for excellence and trusted by customers worldwide. "
        f"Get in touch with us today to place your order or learn more! 👇"
    )

    # 2. LOGIC NA GANO AKIN KASUWANCI (Smart Matching)
    
    # Tsarin Hausa: Idan an rubuta Takalma, Saida, ko Kano
    if "takalma" in desc_lower or "saida" in desc_lower or "kano" in desc_lower or "takalmi" in desc_lower:
        hashtags = ["#KanoBusiness", "#TakalmaMasuKyau", "#KanoMarket", "#ArewaFashion"]
        hashtag_str = " ".join(hashtags)
        
        return {
            "facebook": f"Kuna neman takalma masu inganci da ƙarko a garin Kano? Kada ku damu, mun kawo muku mafita! ✨\n\nSanarwa: {desc}.\n\nKayanmu duka masu kyau ne kuma akan farashi mai sauƙi. Yi maza ka turo mana saƙo (DM) don sayen naka yanzu! 🚀\n\n{hashtag_str}",
            "instagram": f"Hanya mafi sauƙi ta yin ado na gari tana fara ne daga takalmin da ka saka. 👟✨\n\nZaɓi mafi kyau: {desc}.\n\nMuna tura kaya duka jihohin Najeriya daga jihar Kano. Latsa link ɗin dake bio ɗinmu don yin magana da mu. 💎\n\n{hashtag_str}",
            "twitter": f"Ingancin takalmi shi ke ƙara wa tafiya fari. 👇\n\nDuba nan: {desc} 🌍\n\nKira mu ko turo saƙo yanzu domin oda! \n\n{hashtag_str}"
        }
        
    # Idan an rubuta na Turanci
    elif "coffee" in desc_lower:
        hashtags = ["#PremiumCoffee", "#OrganicCoffee", "#CoffeeLovers", "#GlobalExport"]
    elif "ginger" in desc_lower or "organic" in desc_lower or "export" in desc_lower:
        hashtags = ["#OrganicExport", "#Agribusiness", "#GlobalTrade", "#HealthyLiving"]
    elif "textile" in desc_lower or "shadda" in desc_lower or "yadi" in desc_lower or "fabric" in desc_lower:
        hashtags = ["#PremiumFabrics", "#TextileIndustry", "#FashionBusiness", "#TraditionalWear"]
    elif "turare" in desc_lower or "perfume" in desc_lower or "kamshi" in desc_lower:
        hashtags = ["#PremiumPerfumes", "#LuxuryFragrance", "#PerfumeLovers", "#ClassySmell"]
    elif "trading" in desc_lower or "forex" in desc_lower or "nas100" in desc_lower or "crypto" in desc_lower:
        hashtags = ["#FinancialFreedom", "#SmartTrading", "#MarketAnalysis", "#TradingStrategy"]

    hashtag_str = " ".join(hashtags)
    
    # Mayar da sakamakon Turanci tare da hashtags ɗinsu
    return {
        "facebook": f"{facebook_post}\n\n{hashtag_str}",
        "instagram": f"{instagram_caption}\n\n{hashtag_str}",
        "twitter": f"{twitter_post}\n\n{hashtag_str}"
    }