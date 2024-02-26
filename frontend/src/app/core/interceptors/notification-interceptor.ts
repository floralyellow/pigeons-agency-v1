import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpEvent,
  HttpHandler,
  HttpRequest,
  HttpResponse
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { MessagesService } from '../../core/services/messages.service';

@Injectable()
export class NotificationInterceptor implements HttpInterceptor {
  constructor(private messagesService :MessagesService){}
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(req).pipe(
      tap(event => {
        if (event instanceof HttpResponse && event.status === 200) {
          this.messagesService.updateMessageNumber(event.body.message.user.player.nb_notifs);
        }
      })
    );
  }
}
