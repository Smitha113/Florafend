def get_recommendation(disease):
    normalized_disease = disease.lower().replace(' ', '_')

    if normalized_disease == 'apple__apple_scab':
        return [
            "Prune to improve air circulation and reduce humidity.",
            "Apply fungicides preventively during early spring.",
            "Choose apple varieties resistant to scab."
        ]
    elif normalized_disease == 'apple_black_rot':
        return [
            "Prune to improve air circulation and reduce disease pressure.",
            "Apply fungicides during bloom and growing season.",
            "Remove and destroy infected fruit mummies and cankers."
        ]
    elif normalized_disease == 'apple_cedar_apple_rust':
        return [
            "Remove infected leaves and stems to reduce disease spread.",
            "Apply fungicides during spring to prevent initial infections.",
            "Plant resistant apple varieties if possible."
        ]
    elif normalized_disease == 'apple_healthy':
        return [
            "Continue regular care and maintenance practices for healthy apple trees.",
            "Monitor for early signs of disease or pests.",
            "Maintain proper nutrition and watering practices."
        ]
    elif normalized_disease == 'blueberry_healthy':
        return [
            "Monitor for pests and diseases regularly.",
            "Prune to promote air circulation and sunlight exposure.",
            "Apply organic mulch to maintain soil moisture and health."
        ]
    elif normalized_disease == 'cherry(including_sour)__healthy':
        return [
            "Prune regularly to remove dead or diseased branches.",
            "Apply fungicides preventively during wet seasons.",
            "Monitor for pests such as aphids and scale insects."
        ]
    elif normalized_disease == 'cherry(including_sour)__powdery_mildew':
        return [
            "Apply fungicides at the first sign of powdery mildew.",
            "Prune to improve air circulation and reduce humidity around the tree.",
            "Plant cherry varieties resistant to powdery mildew."
        ]
    elif normalized_disease == 'corn(maize)__cercospora_leaf_spot_gray_leaf_spot':
        return [
            "Rotate crops to reduce the buildup of pathogens in the soil.",
            "Apply fungicides preventively during humid conditions.",
            "Choose corn hybrids with resistance to Cercospora leaf spot."
        ]
    elif normalized_disease == 'corn(maize)__common_rust':
        return [
            "Plant resistant corn varieties if available in your area.",
            "Apply fungicides before the disease appears in the field.",
            "Use crop rotation and avoid planting corn in consecutive years."
        ]
    elif normalized_disease == 'corn_(maize)__healthy':
        return [
            "Maintain proper soil fertility and crop nutrition.",
            "Control weeds and pests that can weaken corn plants.",
            "Monitor for signs of nutrient deficiency or stress."
        ]
    elif normalized_disease == 'corn(maize)__northern_leaf_blight':
        return [
            "Use crop rotation and avoid planting corn in the same field consecutively.",
            "Apply fungicides when weather conditions favor disease development.",
            "Plant corn hybrids with resistance to Northern Leaf Blight."
        ]
    elif normalized_disease == 'grape_black_rot':
        return [
            "Prune grape vines to improve air circulation and sunlight exposure.",
            "Apply fungicides preventively during wet seasons.",
            "Remove and destroy infected plant parts to reduce disease spread."
        ]
    elif normalized_disease == 'grape_esca(black_measles)':
        return [
            "Prune grape vines during dormancy to remove infected wood.",
            "Apply fungicides preventively during the growing season.",
            "Manage vineyard hygiene to reduce disease pressure."
        ]
    elif normalized_disease == 'grape__healthy':
        return [
            "Maintain proper vineyard management practices.",
            "Monitor for pests and diseases regularly.",
            "Ensure adequate soil nutrition and water management."
        ]
    elif normalized_disease == 'grape_leaf_blight(isariopsis_leaf_spot)':
        return [
            "Apply fungicides preventively during periods of high humidity.",
            "Prune to improve air circulation and reduce disease incidence.",
            "Monitor for early signs of leaf blight and treat promptly."
        ]
    elif normalized_disease == 'orange__haunglongbing(citrus_greening)':
        return [
            "Remove and destroy infected trees to prevent disease spread.",
            "Apply insecticides to control psyllid vectors.",
            "Use certified disease-free nursery stock for new plantings."
        ]
    elif normalized_disease == 'peach__bacterial_spot':
        return [
            "Apply copper-based fungicides during the dormant season.",
            "Prune to improve air circulation and sunlight exposure.",
            "Remove and destroy infected plant material to reduce disease spread."
        ]
    elif normalized_disease == 'peach_healthy':
        return [
            "Maintain regular pruning to remove dead or diseased wood.",
            "Monitor for pests such as aphids and scale insects.",
            "Apply balanced fertilizer to maintain tree health."
        ]
    elif normalized_disease == 'pepper,_bell_bacterial_spot':
        return [
            "Apply copper-based fungicides early in the season.",
            "Avoid overhead irrigation to reduce disease spread.",
            "Rotate crops with non-host plants to break disease cycles."
        ]
    elif normalized_disease == 'pepper,_bell_healthy':
        return [
            "Monitor for aphids, thrips, and other pests regularly.",
            "Apply balanced fertilizer to promote healthy plant growth.",
            "Prune to remove old or diseased branches."
        ]
    elif normalized_disease == 'potato_early_blight':
        return [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Rotate crops with non-host plants to reduce pathogen buildup.",
            "Monitor soil moisture and avoid overhead irrigation."
        ]
    elif normalized_disease == 'potato_healthy':
        return [
            "Practice crop rotation with non-host plants.",
            "Monitor for potato pests such as Colorado potato beetles.",
            "Apply balanced fertilizer to maintain soil fertility."
        ]
    elif normalized_disease == 'potato_late_blight':
        return [
            "Apply fungicides containing chlorothalonil or mancozeb preventively.",
            "Practice good field hygiene to remove infected potato debris.",
            "Monitor weather conditions and irrigation practices to reduce disease risk."
        ]
    elif normalized_disease == 'raspberry_healthy':
        return [
            "Prune raspberry canes to improve air circulation.",
            "Apply fungicides preventively during periods of high humidity.",
            "Monitor for pests such as aphids and raspberry cane borers."
        ]
    elif normalized_disease == 'soybean_healthy':
        return [
            "Rotate soybean crops with non-host plants.",
            "Monitor for soybean pests such as aphids and soybean cyst nematodes.",
            "Apply balanced fertilizer to maintain soil fertility."
        ]
    elif normalized_disease == 'squash_powdery_mildew':
        return [
            "Plant resistant squash varieties if available.",
            "Apply fungicides containing sulfur or potassium bicarbonate.",
            "Prune to improve air circulation and reduce humidity around plants."
        ]
    elif normalized_disease == 'strawberry_healthy':
        return [
            "Monitor for pests such as aphids and spider mites.",
            "Apply balanced fertilizer to promote healthy strawberry plants.",
            "Mulch around plants to maintain soil moisture and reduce weeds."
        ]
    elif normalized_disease == 'strawberry_leaf_scorch':
        return [
            "Remove and destroy infected leaves to reduce disease spread.",
            "Apply fungicides containing copper hydroxide or mancozeb.",
            "Monitor irrigation practices to avoid excessive moisture."
        ]
    elif normalized_disease == 'tomato_bacterial_spot':
        return [
            "Apply copper-based fungicides early in the season.",
            "Prune tomato plants to improve air circulation.",
            "Use drip irrigation instead of overhead irrigation."
        ]
    elif normalized_disease == 'tomato_early_blight':
        return [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Rotate tomato crops with non-host plants.",
            "Prune tomato plants to improve air circulation."
        ]
    elif normalized_disease == 'tomato_healthy':
        return [
            "Rotate tomato crops with non-host plants.",
            "Monitor for pests such as tomato hornworm and whiteflies.",
            "Apply balanced fertilizer to promote healthy plant growth."
        ]
    elif normalized_disease == 'tomato_late_blight':
        return [
            "Apply fungicides preventively during periods of wet weather.",
            "Remove and destroy infected tomato plants to reduce disease spread.",
            "Avoid overhead irrigation to minimize disease spread."
        ]
    elif normalized_disease == 'tomato_leaf_mold':
        return [
            "Apply fungicides containing copper or sulfur.",
            "Prune to improve air circulation and reduce humidity around tomato plants.",
            "Water tomato plants at the base to avoid wetting foliage."
        ]
    elif normalized_disease == 'tomato_septoria_leaf_spot':
        return [
            "Apply fungicides containing chlorothalonil or copper.",
            "Prune lower tomato leaves to improve air circulation.",
            "Mulch around tomato plants to reduce soil splash."
        ]
    elif normalized_disease == 'tomato_spider_mites_two-spotted_spider_mite':
        return [
            "Monitor for spider mite populations regularly.",
            "Spray affected tomato plants with insecticidal soap.",
            "Improve humidity levels around tomato plants to discourage spider mites."
        ]
    elif normalized_disease == 'tomato_target_spot':
        return [
            "Apply fungicides containing chlorothalonil or mancozeb.",
            "Prune to improve air circulation and reduce disease pressure.",
            "Remove and destroy affected tomato leaves and plant debris."
        ]
    elif normalized_disease == 'tomato_tomato_mosaic_virus':
        return [
            "Control aphid populations to prevent virus transmission.",
            "Plant virus-resistant tomato varieties.",
            "Remove and destroy infected tomato plants and weeds."
        ]
    elif normalized_disease == 'tomato__tomato_yellow_leaf_curl_virus':
        return [
            "Control whitefly populations to reduce virus transmission.",
            "Use virus-resistant tomato varieties if available.",
            "Remove and destroy infected tomato plants and weeds promptly."
        ]
    # Add more elif blocks for other diseases as per your requirement

    # If the disease doesn't match any of the above conditions, return an empty list
    return []
