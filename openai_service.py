import time

def generate_social_posts(business_description, tone, business_goal, content_length, cta_style):
    """
    Brightins AI Engine
    - Pure English Interface
    - Auto-detects Hausa/English input seamlessly
    """
    time.sleep(1.2) # AI Simulation delay
    
    desc = business_description.strip() if business_description.strip() else "our premium products"
    desc_lower = desc.lower()
    
    # Auto-detect Hausa keywords
    hausa_keywords = ["takalma", "saida", "kano", "turare", "yadi", "shadda", "atamfa", "kaya", "kudi", "maka", "kuna", "mun", "ina", "tsada", "bunkasa", "kasuwanci"]
    is_hausa = any(word in desc_lower for word in hausa_keywords)
    
    if is_hausa:
        cta_dict = {
            "Soft CTA": "Muna son jin ra'ayoyinku a sashen comment! 👇",
            "Strong Sales CTA": "YI MAZA KA SAYI NAKA YANZU! Kaya sun kusa ƙarewa, kada a ba ka labari! 🚨",
            "WhatsApp CTA": "Latsa nan domin yin magana da mu kai tsaye a WhatsApp: https://wa.me/2348000000000 📲",
            "DM CTA": "Turo mana saƙon gaggawa (DM) yanzu a nan don ka mallaki naka! 📥"
        }
        length_intro = {
            "Short": f"Gajeren tallanmu akan: {desc}.",
            "Medium": f"Kuna neman mafi kyau? Ga cikakken bayani akan {desc}. Muna tabbatar muku da inganci da gaskiya a kowane lokaci domin gamsuwarku.",
            "Long": f"Barka da zuwa! Idan kuna neman inganci, ƙarko, da gamsuwa na gaskiya, wannan bayanin naku ne.\n\nAbubuwan da suka sa '{desc}' ya fita daban a kasuwa:\n1. Inganci na gaba-da-gaba (Premium Quality).\n2. Farashi mai sauƙi domin kowa.\n3. Amintaccen sabis da saurin tura kaya.\n\nKada ku sake a ba ku labari wajen neman kayan arziki."
        }
        hashtags = "#Kasuwanci #Kano #Inganci #Arewa"
        
        fb = f"{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        ig = f"✨ Kasuwancinmu na gari ✨\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        tw = f"{length_intro['Short'] if content_length == 'Long' else length_intro[content_length]}\n\n{cta_dict[cta_style]} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - Daƙiƙa 60]\nTone: {tone}\n\n[0-15s - HOOK]: (Fito da fara'a da kuzari) 'Tsaya ka saurara! Idan kana son bunkasa kasuwancinka a Intanet, wannan bidiyon naka ne!'\n\n[15-45s - BODY]: 'Ga babban dalilin da ya sa kowa ke magana akan {desc}. Yana da sauƙi da inganci.'\n\n[45-60s - CTA]: '{cta_dict[cta_style]}'"
    
    else:
        cta_dict = {
            "Soft CTA": "Let us know your thoughts in the comments below! 👇",
            "Strong Sales CTA": "BUY NOW! Limited stock available. Don't miss out on this exclusive offer! 🚨",
            "WhatsApp CTA": "Chat with us directly on WhatsApp for instant orders: https://wa.me/2348000000000 📲",
            "DM CTA": "Send us a Direct Message (DM) right now to place your order! 📥"
        }
        length_intro = {
            "Short": f"Quick look at our premium product: {desc}.",
            "Medium": f"Looking for the ultimate solution to elevate your lifestyle? Introducing '{desc}'. Crafted with precision and engineered to deliver top-notch results just for you.",
            "Long": f"Welcome to the next level of excellence. If you value premium quality, long-lasting durability, and maximum satisfaction, you are in the right place.\n\nWhy choose '{desc}':\n1. Unmatched Premium Quality.\n2. Globally Trusted & Certified.\n3. Budget-Friendly & Highly Affordable.\n\nDon't compromise on your standards when you can have the very best today."
        }
        hashtags = "#BusinessGrowth #PremiumQuality #Innovation"
        
        fb = f"🚀 [Brightins AI Generated Post]\nTone: {tone} | Goal: {business_goal}\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        ig = f"✨ Quality meets excellence. ✨\n\n{length_intro[content_length]}\n\n{cta_dict[cta_style]}\n\n{hashtags}"
        tw = f"{length_intro['Short'] if content_length == 'Long' else length_intro[content_length]}\n\n{cta_dict[cta_style]} {hashtags}"
        tt = f"🎥 [TikTok/Shorts Script - 60 Seconds]\nTone: {tone}\n\n[0-15s - HOOK]: (Look directly at the camera with energy) 'Stop scrolling if you want to elevate your business today!'\n\n[15-45s - BODY]: 'Here is why everyone is talking about {desc}. It is simple, effective, and designed just for you.'\n\n[45-60s - CTA]: '{cta_dict[cta_style]}'"

    return {"facebook": fb, "instagram": ig, "twitter": tw, "tiktok": tt}