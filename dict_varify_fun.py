def checkDictionary(input_dict):
    result = None
    default_dict = {
        "job_run_id": "dummy_job_run_id",
        "job_name": "dummy_job_name",
        "impacted_records_count": 1000,
        "valid_records_count": 950,
        "invalid_records_count": 50,
        "comments": "dummy_comments"
    }
    for key, value in input_dict.items():
        if key not in default_dict:
            raise KeyError("New metric {}".format(key))
        elif type(input_dict[key]) != type(value):
            raise TypeError("Incorrect data type for metric {}".format(key))

    return input_dict


sample_input3 = {
    "job_run_id": "dummy_job_run_id",
    "job_name": "dummy_job_name",
    "impacted_records_count": 1000,
    "valid_records_count": 1000,
    "invalid_records_count": 0,
    "comments": "dummy_comments",
    "some_new_key": "some_value"
}


print(checkDictionary(sample_input3))


