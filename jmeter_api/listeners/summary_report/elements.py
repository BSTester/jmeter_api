from jmeter_api.basics.listener.elements import ResultCollector


class SummaryReport(ResultCollector):

    TEMPLATE = '../../basics/listener/result_collector_template.xml'
    
    def __init__(self, *,
                 error_logging: bool = False,
                 filename: str = None,
                 time: bool = True,
                 latency: bool = True,
                 timestamp: bool = True,
                 success: bool = True,
                 label: bool = True,
                 code: bool = True,
                 message: bool = True,
                 thread_name: bool = True,
                 data_type: bool = True,
                 encoding: bool = False,
                 assertions: bool = False,
                 subresults: bool = True,
                 response_data: bool = False,
                 sampler_data: bool = False,
                 xml: bool = False,
                 field_names: bool = True,
                 response_headers: bool = False,
                 request_headers: bool = False,
                 response_data_on_error: bool = False,
                 save_assertion_results_failure_message: bool = False,
                 bytes_: bool = True,
                 sent_bytes: bool = True,
                 url: bool = True,
                 thread_counts: bool = True,
                 idle_time: bool = True,
                 connect_time: bool = True,
                 name: str = 'Summary Report',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        ResultCollector.__init__(self,
            guiclass='SummaryReport',
            error_logging=error_logging,
            filename=filename,
            time=time,
            latency=latency,
            timestamp=timestamp,
            success=success,
            label=label,
            code=code,
            message=message,
            thread_name=thread_name,
            data_type=data_type,
            encoding=encoding,
            assertions=assertions,
            subresults=subresults,
            response_data=response_data,
            sampler_data=sampler_data,
            xml=xml,
            field_names=field_names,
            response_headers=response_headers,
            request_headers=request_headers,
            response_data_on_error=response_data_on_error,
            save_assertion_results_failure_message=save_assertion_results_failure_message,
            bytes_=bytes_,
            sent_bytes=sent_bytes,
            url=url,
            thread_counts=thread_counts,
            idle_time=idle_time,
            connect_time=connect_time,
            name=name,
            comments=comments,
            is_enabled=is_enabled)
