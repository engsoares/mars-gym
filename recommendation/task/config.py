from recommendation.data import InteractionsMatrixDataset, InteractionsDataset, InteractionsAndContentDataset, \
    CriteoDataset, \
    BinaryInteractionsWithOnlineRandomNegativeGenerationDataset, \
    UserTripletContentWithOnlineRandomNegativeGenerationDataset, \
    UserTripletWithOnlineRandomNegativeGenerationDataset, \
    UserTripletWeightedWithOnlineRandomNegativeGenerationDataset,\
    IntraSessionTripletWithOnlineRandomNegativeGenerationDataset, \
    IntraSessionTripletWithOnlineProbNegativeGenerationDataset,\
    ContextualBanditsDataset
from recommendation.task.data_preparation import yelp, ifood, criteo
from recommendation.task.meta_config import *

PROJECTS: Dict[str, ProjectConfig] = {
    "criteo": ProjectConfig(
        base_dir=criteo.BASE_DIR,
        prepare_data_frames_task=criteo.PrepareDataFrames,
        dataset_class=CriteoDataset,
        input_columns=[Column('dense', IOType.ARRAY), Column('categories', IOType.ARRAY)],
        output_column=Column("TARGET", IOType.NUMBER),
        recommender_type=RecommenderType.CONTENT_BASED,
    ),
    "yelp": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpRatingsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("user_idx", IOType.INDEX), Column("business_idx", IOType.INDEX)],
        output_column=Column("stars", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_user_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllUserRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_business", IOType.ARRAY)],
        output_column=Column("stars_per_business", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_user_binary_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllUserBinaryRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_business", IOType.ARRAY)],
        output_column=Column("stars_per_business", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_business_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllBusinessRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_user", IOType.ARRAY)],
        output_column=Column("stars_per_user", IOType.ARRAY),
        recommender_type=RecommenderType.ITEM_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_with_shift_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX),
                       Column("mode_shift_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_with_shift_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        possible_negative_indices_columns={
            "merchant_idx": ["weekday breakfast", "weekday dawn", "weekday dinner", "weekday lunch",
                             "weekday snack", "weekend breakfast", "weekend dawn", "weekend dinner",
                             "weekend lunch", "weekend snack"]
        },        
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX),
                       Column("mode_shift_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),    
    "ifood_binary_buys_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        possible_negative_indices_columns={
            "merchant_idx": ["weekday breakfast", "weekday dawn", "weekday dinner", "weekday lunch",
                             "weekday snack", "weekend breakfast", "weekend dawn", "weekend dinner",
                             "weekend lunch", "weekend snack"]
        },
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),    
    "ifood_binary_buys_and_buys_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_and_buys_and_visits_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_and_buys_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_and_buys_and_visits_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_and_buys_and_visits_and_time_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX),
                        Column("mode_shift_idx", IOType.INDEX), Column("mode_day_of_week", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),    


    "ifood_session_triplet_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodIntraSessionInteractionsDataFrames,
        dataset_class=IntraSessionTripletWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("merchant_idx_A", IOType.INDEX), Column("merchant_idx_B", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        # possible_negative_indices_columns={
        #     "merchant_idx": ["weekday breakfast", "weekday dawn", "weekday dinner", "weekday lunch",
        #                      "weekday snack", "weekend breakfast", "weekend dawn", "weekend dinner",
        #                      "weekend lunch", "weekend snack"]
        # },
        metadata_columns=[Column("trading_name", IOType.ARRAY), Column("description", IOType.ARRAY),
                          Column("category_names", IOType.ARRAY), Column("menu_full_text", IOType.ARRAY), 
                          Column("restaurant_complete_info", IOType.ARRAY)],
        auxiliar_output_columns=[Column("relative_pos", IOType.NUMBER), Column("prob", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),     
    "ifood_session_triplet_with_search_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodIntraSessionInteractionsDataFrames,
        dataset_class=IntraSessionTripletWithOnlineProbNegativeGenerationDataset,
        input_columns=[Column("merchant_idx_A", IOType.INDEX), Column("merchant_idx_B", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        possible_negative_indices_columns={},
        metadata_columns=[Column("trading_name", IOType.ARRAY), Column("description", IOType.ARRAY),
                          Column("category_names", IOType.ARRAY), Column("menu_full_text", IOType.ARRAY), 
                          Column("restaurant_complete_info", IOType.ARRAY)],
        auxiliar_output_columns=[Column("relative_pos", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),    
    "ifood_binary_buys_triplet_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=UserTripletWithOnlineRandomNegativeGenerationDataset,
        possible_negative_indices_columns={
            "merchant_idx": ["weekday breakfast", "weekday dawn", "weekday dinner", "weekday lunch",
                             "weekday snack", "weekend breakfast", "weekend dawn", "weekend dinner",
                             "weekend lunch", "weekend snack"]
        },
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_buys_visits_triplet_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=UserTripletContentWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_content_triplet_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodInteractionsDataFrames,
        dataset_class=UserTripletContentWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        possible_negative_indices_columns={
            "merchant_idx": ["weekday breakfast", "weekday dawn", "weekday dinner", "weekday lunch",
                             "weekday snack", "weekend breakfast", "weekend dawn", "weekend dinner",
                             "weekend lunch", "weekend snack"]
        },
        metadata_columns=[Column("trading_name", IOType.ARRAY), Column("description", IOType.ARRAY),
                          Column("category_names", IOType.ARRAY), Column("restaurant_complete_info", IOType.ARRAY)],
        output_column=Column("binary_buys", IOType.NUMBER),
        auxiliar_output_columns=[Column("buys", IOType.NUMBER), Column("visits", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_user_cdae": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodAccountMatrixWithBinaryBuysDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("buys_per_merchant", IOType.ARRAY)],
        output_column=Column("buys_per_merchant", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_item_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodMerchantMatrixWithBinaryBuysAndContentDataFrames,
        dataset_class=InteractionsAndContentDataset,
        input_columns=[Column("buys_per_merchant", IOType.ARRAY), Column("account_idx", IOType.INDEX)],
        output_column=Column("buys_per_merchant", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_contextual_bandit": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodSessionsDataFrames,
        dataset_class=ContextualBanditsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX),
                        Column("hist_visits", IOType.NUMBER), Column("hist_buys", IOType.NUMBER)],
        metadata_columns=[Column("trading_name", IOType.ARRAY), Column("description", IOType.ARRAY),
                          Column("category_names", IOType.ARRAY), Column("restaurant_complete_info", IOType.ARRAY)],
        output_column=Column("buy", IOType.NUMBER),
        auxiliar_output_columns=[Column("ps", IOType.NUMBER)],
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
}
