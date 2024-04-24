# importing the joblib libraray
import joblib

dict_cat = {'deplist_bath_body' : ['Bath & Shower', 'Bath Soaks & Bubble Bath', 'Body Lotions & Body Oils', 'Body Moisturizers', 'Body Products', 'Body Sprays & Deodorant',
                                    'Body Sunscreen', 'Body Wash & Shower Gel', 'Cellulite & Stretch Marks', 'Deodorant & Antiperspirant', 'Deodorant for Men', 'For Body', 
                                    'For Face', 'Hand Cream & Foot Cream', 'Lotions & Oils', 'Scrub & Exfoliants', 'Self Tanners', 'Wellness'],
                'deplist_fragrance' : ['Body Mist & Hair Mist', 'Candles', 'Candles & Home Scents', 'Cologne', 'Diffusers', 'Perfume', 'Rollerballs & Travel Size'],
                'deplist_gifts' : ['Cologne Gift Sets', 'Perfume Gift Sets', 'Value & Gift Sets'],
                'deplist_hair' : ['Color Care', 'Conditioner', 'Dry Shampoo', 'Hair Masks', 'Hair Oil', 'Hair Primers', 'Hair Products', 'Hair Spray', 
                                'Hair Styling & Treatments', 'Hair Styling Products', 'Hair Thinning & Hair Loss', 'Leave-In Conditioner', 'Scalp & Hair Treatments', 
                                'Shampoo', 'Shampoo & Conditioner'],
                'deplist_makeup' : ['BB & CC Cream', 'BB & CC Creams', 'Blush', 'Bronzer', 'Color Correct', 'Concealer', 'Contour', 'Eye Palettes', 'Eye Primer', 
                                    'Eye Sets', 'Eyebrow', 'Eyeliner', 'Eyeshadow', 'Face Primer', 'Face Sets', 'False Eyelashes', 'Foundation', 'Highlighter', 
                                    'Lip Gloss', 'Lip Liner', 'Lip Plumper', 'Lip Sets', 'Lip Stain', 'Lip Sunscreen', 'Lip Treatments', 'Lipstick', 'Liquid Lipstick', 
                                    'Makeup Palettes', 'Makeup Removers', 'Mascara', 'Nail', 'Setting Spray & Powder'],
                'deplist_mini' : ['Bath & Body', 'Fragrance', 'Hair', 'Makeup', 'Mini Size', 'Skincare'],
                'deplist_others' : ['no category'],
                'deplist_skincare' : ['After Sun Care', 'Aftershave', 'Anti-Aging', 'Beauty Supplements', 'Blemish & Acne Treatments', 'Decollete & Neck Creams', 
                                    'Exfoliators', 'Eye Cream', 'Eye Creams & Treatments', 'Eye Masks', 'Face Masks', 'Face Oils', 'Face Serums', 'Face Sunscreen', 
                                    'Face Wash', 'Face Wash & Cleansers', 'Face Wipes', 'Facial Peels', 'Hair Removal & Shaving', 'Holistic Wellness', 
                                    'Lip Balm & Treatment', 'Lip Balms & Treatments', 'Mists & Essences', 'Moisturizer & Treatments', 'Moisturizers', 'Night Creams', 
                                    'Shaving', 'Sheet Masks', 'Skincare Sets', 'Sunscreen', 'Teeth Whitening', 'Tinted Moisturizer', 'Toners'],
                'deplist_tools_brushes' : ['Accessories', 'Blotting Papers', 'Brush Cleaners', 'Brush Sets', 'Cheek Palettes', 'Cleansing Brushes', 'Curling Irons', 
                                        'Curls & Coils', 'Eye Brushes', 'Eyelash Curlers', 'Face Brushes', 'Facial Cleansing Brushes', 'Facial Rollers', 'Hair Accessories',
                                        'Hair Brushes & Combs', 'Hair Dryers', 'Hair Removal', 'Hair Straighteners & Flat Irons', 'High Tech Tools', 'Lid Shadow Brush',
                                        'Lip Brushes', 'Makeup & Travel Cases', 'Makeup Bags & Travel Cases', 'Mirrors & Sharpeners', 'Powder Brush', 'Spa Tools',
                                        'Sponges & Applicators', 'Tweezers & Eyebrow Tools']}

joblib.dump(dict_cat, 'dict_cat.joblib')
